1. To read the a csv file and create a DF, where the date column is recognized as 'String', but I want it to be 'Timestamp'?

Solution: Databrick is Used
-When we don't mention any formatting/inferschema,
df=spark.read.format("csv").option("header","true").load("<path>")
df.printSchema() ##It shows date as string
df.display()
-When we mention inferSchema as true,
df=spark.read.format("csv").option("header","true").option("inferSchema","true").load("<path>")
df.printSchema() ##Even now it shows date as string
df.display()
-When we mention the formatting,
df=spark.read.formt("csv").option("header","true").option("inferSchema","true").option("timestampFormat","M/d/yyyy").load("<path>")
df.printSchema() ##It shows date as timestamp, but works if everything is in "M/d/yyyy" format, what if it is in any other format??
df.display()
-Best way is to use Struct Schema,
from pyspark.sql.types import *
schema=StructType([
    StructField("Customer_No",IntegerType(),True),
    StructField("Card_type",StringType(),True),
    StructField("Date",DateType(),True),
    StructField("Category",StringType(),True),
    StructField("TransactionType",StringType(),True),
    StructField("Amount",DoubleType(),True)
])

df=spark.read.format("csv").option("header",True).option("dateformat","M/d/yyyy").schema(schema).load("<path>")
df.printSchema() ##This works, this will print it as a date
df.display()

======================================================

2. Read the input testFile (Pipe delimited) provided as a "Spark RDD" and no DF/Dataset to be used
Remove the Header Record from the RDD
Calculate Final_Price: Final_Price=(Size * Price_SQ_FT)
Save the final rdd into TextFile with header is pipe delimited,
Property_ID|Location|Final_Price

Solution: Jupyter Note-Book is being used
import findspark
findspark.init()
##Let's create a SparkSession and SparkContext
import pyspark.sql import SparkSession
spark=SparkSession.builder.appName("CodingWithRDD").master("local[*]").getOrCreate()
sc=spark.sparkContext ##Creates a SparkContext
spark.version ##To know the version 
##To read the input file as RDD using the Spark Context
rdd_in = sc.textFile("input.txt")
##Apply filter to get header and data
rdd1=rdd_in.filter(lambda l: not l.startswith("Property_ID"))
header=rdd_in.filter(lambda l: l.startswith("Property_ID"))
##Apply Map and FlatMap to get the column data
rdd2=rdd1.flatMap(lambda x:x.split(',')).map(lambda x:x.split('|')) ##FlatMap is used to split textFile with commas (mainly line differentiation) and later map to split columns based on pipeline (mainly for Column differentiation)
rdd2.take(4)
[['1494234', 'Santa Bay', '90900', '4', '4', '3540', '286.78', 'Short Sale']]
##Get the index of the required column
col_list=header.first().split('|')
f1=col_list.index("Property_ID")
f2=col_list.index("Location")
f3=col_list.index("Size")
f4=col_list.index("Price_SQ_FT")
##Function definition to calculate the final price
def mul_price(d1,d2):
    res=float(d1)*float(d2)
    return str(res)    
##Call the function and create final result as expected
header_out=header.map(lambda x:x.split("|")[f1]+"|"+x.split("|")[f2]+"|Final_Price")
rdd3=rdd2.map(lambda x:x[f1]+"|"+x[f2]+"|"+mul_price(x[f3],x[f4]))
final_out=header_out.union(rdd3)
##Save the final Spark RDD as textFile
final_out.collect()
final_out.coalesce(1).saveAsTextFile("output.txt")

================================================================

3. Apache Spark OOM - Out Of Memory, let's understand Driver OOM with Demo
Solution:
-OOM can occur in both Driver as well as Executors, both has their own reasons
-Driver OOM is due to,
    -Collect() on top of large dataset
    -Broadcast join that doesn't fit into memoryview
    -Operations based on native python (Like usage of Pandas, this is handled in Driver) or R
Trying collect() OOM
df=spark.range(1000)
df.show() ##This will print the data frame
df=spark.range(1000000)
df.show() ##OutOfMemoryError
Mitigation for OOM issue:
    -To increase the Driver Memory
    -To avoid certain actions that pulls data into Driver Memory

===============================================================

4. Consider we have CSV files in several folders (in recursive manner) as shown in the figure.
How will you read all the CSV file at a time and load them into spark dataframe?
##Creating a dataframe by reading a file
df1 = spark.read.format("csv").option("header","true").load("<ParentPath>")
display(df1)
##Adding a column to know from which filename the record is fetched
from pyspark.sql.functions import input_file_name
df1=spark.read.format("csv").option("header","true").load("<ParentPath>").withColumn("filename",input_file_name())
display(df1) ##This won't read data from subfolders
##To read the data from multiple paths we have two options
##Method1: Hardcode all the recursive path available to read
in_path=["<path1>","<path2>"...]
df1=spark.read.format("csv")..option("header","true").load(inpath)
display(df1)##This will give all the data from given paths, can be checked using input_file_name()
##Method2: Best method, use recursive option to read all at once
df1=spark.read.format("csv").option("recursiveFileLookup","true").option("header","true").load("<ParentPath>").withColumn("FileName",input_file_name())
display(df1)
#***********Note: The input path shouldn't be partition specific, if it is a partitioned then it will thrown an exception

==================================================================

5. Difference between Repartition(Col) and PartitionBy(Col):
Solution:
in_df=spark.read.option("header","true").csv("<path1>")
display(in_df)
##Let's get num of partition by converting df to rdd first
in_df.rdd.getNumPartitions() ##Output is 1
in_df.select("Customer_No").distinct().display()##Seven unique records
in_df.count()
##Basic Difference b/w the two
in_df.repartition(3).rdd.getNumPartitions() ##This upscale/downgrade the number of partitions depending on it's earlier value
in_df.repartition("Customer_No").rdd.getNumPartitions() ##We can also give colname, therefore using the col it will create partitions, not mandatory that it should only create 7, Spark is brilliant enough to take care by itself and also spark makes sure the number of records belonging to unique customer_no resides in same partition, bingo!
in_df.repartition(3,"Customer_No").rdd.getNumPartitions() ##Manually giving partitions
##To know how many records available in each partition
from pyspark.sql.functions import spark_partition_id
in_df.repartition(3,"Column_No").withColumn("Partition_Id",spark_partition_id).groupBy("Partition_Id").count().display()
##Partition By is not available for DF, instead possible at time of writing as seen below:
in_df.write.partitionBy("Customer_No") ##No facility to give column names

##Functional Difference:
in_df.repartition("Customer_No").write.format("csv").option("header","true").mode("overwrite").save("<path1>")
in_df.write.partitionBy("Customer_No").format("csv").option("header","true").mode("overwrite").save("<path2>")

##********When we use repartition it will make use of Spark Memory, where as the partitionBy stores data onto disk
##********Repartition involves shuffle in Ram memory for partitioning data, whereas partitionBY doesn't involve shuffle, instead pushes data directly to target path and creates a partition in the disk

##Performance after writing to data to target:
inpart=spark.read.csv("<target_path of partitionBy>",header=True).filter("Customer_no=1000210")
in_part.display() ##Output is faster here
in_df.filter("Customer_no=1000210").display() ##It is slower (in_df is without any partitionBy or repartition i.e. normal dataframe)

================================================================

6. Consider we have two Files - File1 and File2, with different schema, how will you merge both file into single Dataframe as shown?
##File1:
Name|Age
A|25
B|26
C|28
D|37

##File2:
Name|Age|Gender
E|32|M
F|33|F
G|12|M

##Output Required:
Name    Age     Gender
A       25      null
B       26      null
:
:
G       12      M


Solution:
We can achieve the output, with below approaches,
-WithCOlumn, Union
-Define Schema, Union
-Apply Outer Join
-Automate the process

1st Approach:
============
#Import the findspark while working with the Jupyter-Notebook
import findspark
findspark.init()
#Create SparkSession and import all required packages
from pyspark.sql import SparkSession,types
spark=SparkSession.builder.master("local").appName('Modes of DataFrameReader').getOrCreate()
sc=spark.SparkContext
df1=spark.read.option("delimiter","|").csv("input.csv",header=True)
df1.show()
df2=spark.read.option("delimiter","|").csv("input.csv",header=True)
df2.show()
##Let's perform Union
df1.union(df2) ##This will throw error that union can be performed on the tables with same number of columns
from pyspark.sql.functions import lit
df_add=df1.withColumn("Gender",lit("null"))
df_add.show()
Name    Age     Gender
A       25      null
B       26      null
:
:
##Now we can perform a Union
df1.union(df_add)
Name    Age     Gender
A       25      null
B       26      null
:
:
G       12      M

2nd Approach:
=============
from pyspark.sql.types import *
schema=StructType([StructField("Name",StringType(),True),StructField("Age",IntegerType(),True),StructField("Gender",StringType,True)])
df3=spark.read.option("delimiter","|").csv("<path>",header=True,schema=schema)
df3.show()
df4=spark.read.option("delimiter","|").csv("<path>",header=True,schema=schema)
df3.union(df4).show()
Name    Age     Gender
A       25      null
B       26      null
:
:
G       12      M

3rd Approach:
=============
first_df=spark.read.option("delimiter","|").csv("<path>",header=True)
sec_df=spark.read.option("delimiter","|").csv("<path>",header=True)
df_output=first_df.join(sec_df,on=["Name","Age"],how="Outer")
df_output.show() ##Here the output takes time as it involves shuffle here
Name    Age     Gender
A       25      null
B       26      null
:
:
G       12      M

4th Approach: ##In Real Time there are N number of columns, we can't specifically mention all columns
=============
df1=spark.read.option("delimiter","|").csv("<path>",header=True)
df2=spark.read.option("delimiter","|").csv("<path>",header=True)
##First let's find a difference between df1 and df2 columns, later add missing columns using with COlumns
listA=list(set(df1.columns)-set(df2.columns))
listB=list(set(df2.columns)-set(df1.columns))
for i in listA:
    df2=df2.withColumn(i,lit("null"))
for i in listB:
    df1=df1.withColumn(i,lit("null"))
df1.union(df2).show()
Name    Age     Gender
A       25      null
B       26      null
:
:
G       12      M


================================================================

7. How do you merge the Two Dataframes and when to use Union and UnionbyName?
##UseCase1:
#DF1:
Year  Cast    Movie
2020  Dhanush Karnan
#DF2:
Cast   Year  Movie
Vijay  2020  Master
##Above there are two dataframes and columns are shuffled when one is compared to the other
#OutputRequired:
Year Cast    Movie
2020 Dhanush Karnan
2020 Vijay   Master

##UseCase2:
#DF1:
Year  Cast    Movie
2020  Dhanush Karnan
#DF2:
Cast   Year  Movie  Status
Vijay  2020  Master Successful
##Above there are two dataframes and columns are shuffled when one is compared to the other
#OutputRequired:
Year Cast    Movie  Status
2020 Dhanush Karnan null
2020 Vijay   Master Successful

Solution:
##Manually creating data
list_a=[["2020","Dhanush","Karnan"]]
list_b=[["Vijay","2020","Master"]]
##Creating DataFrame and also hardcoding the schema
in_df1=spark.createDataFrame(list_a,("Year","Cast","Movie"))
in_df2=spark.createDataFrame(list_b,("Cast","Year","Movie"))
in_df1.display()
in_df2.display()
##Let's apply Union : Merge the two dataframe with respect to position of the column and datatype of the column in Data
in_df1.union(in_df2).display() ##Therefore output below is inappropriate
Year    Cast    Movie
2020    Dhanush Karnan
Vijay   2020    Master
##Mitigation
in_df2=in_df2.select("Year","Cast","Movie")
in_df1.union(in_df2).display()
Year Cast    Movie 
2020 Dhanush Karnan
2020 Vijay   Master
##Let's apply UnionByName : Merge the two dataframe with respect Name of the column in Data
indf1.unionByName(in_df2).display() ##This is cool!
Year Cast    Movie 
2020 Dhanush Karnan
2020 Vijay   Master

UseCase2:
##Manually creating data
list_a=[["2020","Dhanush","Karnan"]]
list_b=[["Vijay","2020","Master","Successful"]]
##Creating DataFrame and also hardcoding the schema
in_df1=spark.createDataFrame(list_a,("Year","Cast","Movie"))
in_df2=spark.createDataFrame(list_b,("Cast","Year","Movie","Status"))
in_df1.display()
in_df2.display()
#Let's do Union: 
in_df1.union(in_df2).display() #Will throw error due to column mismatch
#Let's do unionByName: Life seems so simple here
in_df1.unionByName(in_df2,allowMissingColumns=True).display()

=============================================================

8. Consider a Spark Dataframe as shown below, calculate the total balance amount for each customer based on credit and debits as shown in the result below

##Input DF:
Customer_No Card_Type   Date        Category    Transaction_Type    Amount
101         Checking    1/16/2018   Utilities   debit               60
:
:

##Output_DF:
Customer_No     Total_Balance
101             1657.14

#*******Logic : Sum(Credit)-Sum(Debit)

Solution:
df1=spark.read.format("csv").option("header","true").option("infer","schema").load("<path>")
df1.show()
##Method1:
#-Create a column with when to have-1*(debit amount)
#-GroupBy Sum of new column

from pyspark.sql.functions import when,col
df2=df1.withColumn("amount_chk",when(col("TransactionType")=='debit',-1*col("Amount")).otherwise(col("Amount")))

from pyspark.sql.functions import sum
df3=df2.groupBy("Customer_No").agg(sum("amount_chk")).alias("total_balance")
display(df3) ##Therefore this gives the total_balance
Customer_No     Total_Balance
101             1657.14

##Method-2 ##Best Approach
#-Using Pivot to transpose rows into columns and aggregate amount column
#-Calculate difference between credit and debit column

df2=df1.groupBy("Customer_No").pivot("Transaction Type").agg(sum("Amount"))
display(df2)
Customer_No     Credit      Debit
101             2076        796
102             975         9778
:
:
:
df3=df2.withColumn("total_balance",col("credit")-col("debit")).drop("credit","debit")
display(df3)
Customer_No     Total_Balance
101             1657.14

===========================================================

9. Consider a Spark DataFrame as shown below, mask the data in mobile and email column as shown in the result below:

#input_data:
cus#    cusNam  cusAge  email       mobile
101     A       7       ad@gmail.com 12342987

#Output_data
cus#    cusNam  cusAge  email       mobile
101     A       7       a*@gmail.com 12****87

Solution:
#This can be achieved by using an udf function:
#Email-Mask UDF
def mask_email_func(colVal):
    mail_usr=colVal.split("@")[0]
    n=len(mail_usr)
    charList=list(mail_usr)
    charList[1:int(n)-1]='*'*int(n-2)
    out="".join(charList)+"@"+colVal.split("@")[1]
    return out

mask_email_func("mailid_01@gmail.com")
##First watch the UDF portion of this playlist, later come back
   
def mask_mob_func(colVal):
    n=len(colVal)
    charList=list(colVal)
    charList[2:int(n)-2]='x'*int(n-4)
    return "".join(charList)
    
============================================================

10. Consider we have a Spark_DataFrame, how to get the count of each partition in a DataFrame?
Solution:
##This will also helps in understanding the data skewness
data="<path>"
df1=spark.read.format("csv").option("header","true").load(data)
df1.show()
df1.count()
in_data=df1.repartition(4)
in_data.rdd.getNumPartitions() ##4
##Let's get num of records in each partitions:
from pyspark.sql.functions import spark_partition_id
df2=in_data.withColumn("partition_id",spark_partition_id()).groupBy("partition_id").count()
display(df2)
partition_id    count
0               2323
1               2323
2               2531
3               2532

##Let's look for Skew Data, instead of mentioning number of repartitions, let's give a card_category
in_data=df1.repartition(card_category)
in_data.rdd.getNumPartitions() ##200, but data will be in only 3 to 6 partitions max
df2=in_data.withColumn("partition_id",spark_partition_id()).groupBy("partition_id").count()
display(df2)##Data is present in only 4 partitions and most of the data is present in partition_id 128, this will lead to skewness
partition_id    count
38              20
94              555
128             9436
146             116

##****Note: Skewness is taken care in another video, have a look

============================================================

11. Consider we do have some spark operations as shown below, how to get count of dataframe after each operation without using df.count()?

Read Input Data > "Count" > Apply Filter > "Count" > Group By > "Count" > Show

Solution:
fileloaction="<path>"
in_data=spark.read.format("csv").option("header","true").option("inferSchema","true").
option("delimiter",'|').load(file_location)
filter_data=in_data.filter("state_code<>'NY'")
group_data = filter_data.groupBy("City").sum("2019_estimate")

##Accumulators are counter and it's of the shared variable in Spark:
filter_counter=spark.sparkContexrt.accumulator(0)
groupByCounter=spark.sparkCOntextr.accumulator(0)
sourceCounter=spark.sparkContext.accumulator(0)

in_data.foreach(lambda x: sourceCounter.add(1))
filter_data.foreach(lambda x: filterCounter.add(1))
group_data.foreach(lambda x: groupCounter.add(1))

##Accumulators were quite quick, please check
print(sourceCounter.value)
print(filterCounter.value)
print(groupCounter.value)

##Below ones take more time
print(in_data.count())
print(filter_data.count())
print(group_data.count())

============================================================

12. Consider we have a Spark DataFrame named "group_data", what is the best approach to find DataFrame is empty or not??
Solution:
file_location="<path>"
in_data=spark.read.format("csv").option("header","true").option("inferSchema","true").option("delimiter",'|').load(file_location)
group_data=in_data.filter("state_code=='NY'").groupby("city").sum("2019_estimate")
group_data.show() ##It is not null and has some data
if group_data.count() > 0:
    print("True")
else:
    print("False")
#True
if group_data.first():
    print("True")
else:
    print("False")
#True   
if group_data.take(1) > 0:
    print("True")
else:
    print("False")
#True    
##Best Improved Way and faster way:
if group_data.rdd.isEmpty():
    print("False")
else:
    print("True")
#False

============================================================

13. Consider a Spark Dataframe with some duplicate records in it. How will you find all the duplicate records and report it as shown in output dataframe?
****Note: Question is not to drop duplicate, it's to find the duplicate records alone

#Input DataFrame:
Name    Age     Education   Year
A       53      MBA         1985
B       28      BE          2012
A       53      MBA         1985

#Output Dataframe:
Name    Age     Education   Year
A       53      MBA         1985

Solution:
import findspark
findspark.init()
from pyspark.sql import SparkSession
spark=SparkSession.builder.appName("Report Duplicate").getOrCreate()
in_df=spark.read.csv("<path>",header=True)
in_df.show()
##GroupBy - Approach: This will lead to lot and lots of shuffling, all the columns to be mentioned, if col numbers are huge it won't make sense
in_df.groupby("Name","Age","Education","Year").count().where("count>1").drop("count").show()
##Window - Ranking function Approach : Better one
#Ranking Function:
#    -Rank
#    -Dense_Rank
#    -Row_Number
#    -Percent_Rank
#    -ntile
from pyspark.sql.window import Window
from pyspark.sql.functions import col,row_number
win=Window.partitionBy("name").orderBy(col("Year").desc())
in_df.withColumn("row_number",row_number().over(win)).filter("rank>1").drop("rank").dropDuplicates().show()

============================================================

14. Consider a file with delimiter ~|, how will you load it as a spark DataFrame as shown below?
Key Note: 
-Avoid using sparkContext(sc) and use sparkSession(spark)
-Header in the file must be handled
-Multiple delimiter must be handled
-Comma between Name must be taken care
#Input:
Name~|Age
A, B~|26

#Output:
Name    Age
A, B    26

Solution:
import findspark
findspark.init()
from pyspark.sql import SparkSession
spark=SparkSession.builder.appName("Report Duplicate").getOrCreate()
df=spark.read.csv("<filename>")##Doesn't give proper value
##Usage of option("delimiter",'~|'), didn't help
df=spark.read.text("<filename>")
header=df.first()[0]
header ##'Name~|Age'
schema=header.split('~|')
schema ##['Name','Age']
df_input=df.filter(df['value']!=header).rdd.map(lambda x:x[0].split('~|').toDF(schema))
df_input.show(truncate=0)

============================================================

15. What is the Output? map vs flatMap
#Input:
101,Azar,finance
102,Mani,HR
103,Manish,employee
#Question1:
in_rdd=sc.textFile("<filename>")
map_rdd=in_rdd.map(lambda x:x.split(','))
map_rdd.count()
##Output is 3
#Question2:
in_rdd=sc.textFile("<filename>")
map_rdd=in_rdd.flatMap(lambda x:x.split(','))
map_rdd.count()
##Output is 9

###*****Note: Please refer to the pictorical representation in the video

============================================================

16. Filter condition on Date vs Unix Timestsmp:
In general the Unix Timestamp is always faster as it will be in the integer format and aggregation performed will be faster

To convert the input date to unix_timestamp:
from_date='2021-01-01'
to_date='2021-04-30'
import datetime
#Convert String to datetimeformat:
ft_date=datetime.datetime.strptime(from_date,"%Y-%m-%d")
tt_date=datetime.datetime.strptime(ti_date,"%Y-%m-%d")
#Convert datetime to timestamp:
ft_date=int(datetime.datetime.timestamp(f_date))
tt_date=int(datetime.datetime.timestamp(t_date))

in_df=spark.read.csv("<filename>")
in_df.count()

from pyspark.sql.functions import sum
in_df.filter("date>='2021-01-01' and date <= '2021-04-30'").groupby('State/UnionTerritory').agg(sum('Cured')).show()
##Above filter takes more time when we go with actual date, post conversion into unix, things work faster

from pyspark.sql.functions import to_date,max,unix_timestamp
in_df2=in_df.withColumn("U_Date",unix_timestamp("Date",'yyyy-MM-dd'))

in_df2.filter("u_date>=1609439400 and u_date<=1619807340").groupby('State/UnionTerritory').agg(sum('Cured')).show()
##Above gives faster results, because it is in the form integer and also it can easily take help of SQL query engine

#Let's try with automated code:
from pyspark.sql.functions import col
in_df2.filter((col('u_date')>=ft_date) & (col('u_date')<=tt_date)).groupby('State/UnionTerritory').agg(sum('Cured')).show()

============================================================

17. Consider an input text file, holding single row with pipe delimited as shown below. How will you "apply line break to every 5th occurrence of pipe deleimiter" and display as shown below?

input : Azar|BE|8|BigData|9273564531|Student details 2|student details 3......

output:
Name    Edu     YOE     Tech    MobNum
Azar    BE      8       BigData 9273564531
Ramesh  BTech   3       Java    9273564535
:       :       :       .Net    9273564537  
:       :       :       :       :

df=spark.read.csv("input_path")
df.display()
##Apply Regexp to replace | in every 5th occurance
from pyspark.sql.functions import regexp_replace,split,explode
df1=df.withColumn("chk",regexp_replace("_c0","(.*?\\|){5}","$0-"))
df1.display()
df1.show()
##New COlumn chk to be created using reference of _c0, where in _c0 the delimiters can be .*?\\| whatever, at 5th occurence add new delimiter '-'

_c0                                                                      chk
Azar|BE|8|BigData|9273564531|Student details 2|student details 3|......  Azar|BE|8|BigData|9273564531|-Student details 2|-student details 3|-......

##Next step is to explode into multiple records with single column
#When we explode, output will be a list
from pyspark.sql.functions import regexp_replace,split,explode
df2=df1.withColumn('col_explode',explode(split('chk','\|-'))).select('col_explode')
df2.show()

col_explode
Azar|BE|8|BigData|9273564531
Student details 2
Student details 3

##Next step is to split by |, to do this, it's better to convert it into a RDD
rdd_df=df2.select("col_explode").rdd.map(lambda x:x[0].split("|")).collect()
##Output is a list as seen below:
[['Azar','BE','8','BigData','9273564531'],
['Ramesh','BTech','3','Java','9273564532'],
...................
]

##Converting rdd back to df
df3=rdd_df.toDF(["Name","Edu","YOE","Tech","Mobnum"])
df3.show()

Name    Edu     YOE     Tech    MobNum
Azar    BE      8       BigData 9273564531
Ramesh  BTech   3       Java    9273564535
:       :       :       .Net    9273564537  
:       :       :       :       :

============================================================

18. Consider a file with Some corrupt/bad data as shown below. How will you handle those and load into Spark Dataframe?

###Note: It's a good practise to avoid using Filter after reading as DF an try to remove bad data while reading the file itself

input:
Emp_no,Emp_name,Dept
101,Murugan,Healthcare
Invalid Entry,Description:Bad Record entry
102,Kannan,Finance
:
:
Connection lost,Description:Poor Connection
104,Pavan,HR
:
:

output:
Emp_no  Emp_name    Department
101     Murugan     Healthcare
102     Kannan      Finance
103     Mani        IT
104     Pavan       HR

##Ideally there are three Modes in Spark.Read():
PERMISSIVE : This is the default mode
FAILFAST
DROPMALFORMED

import findspark
findspark.init()

##Create SParkSession and import all required packages:
from pyspark.sql import SparkSession,types

spark=SparkSession.builder.master("local").appName("Modes of Dataframereader").getOrCreate()
sc=spark.sparkContext

##Let's read the malformed record without any option, i.e. the permissive mode
df=spark.read.csv('input1.csv',header=True)
df.show()
Emp_no          Emp_name            Department
101             Murugan             HealthCare
Invalid Entry   Description: Bad..  null
:
:

##Let's read the malformed record with failfast mode
df=spark.read.option("mode","FAILFAST").csv('input1.csv',header=True)
df.show()
Py4JJavaError : Malformed CSV Records

##Let's read the malformed record with dropmalformed mode
df=spark.read.option("mode","DROPMALFORMED").csv('input2.csv',header=True)
df.show()
Emp_no  Emp_name    Department
101     Murugan     Healthcare
102     Kannan      Finance
103     Mani        IT
104     Pavan       HR

##While using the Drop Malformed, it's good to define our own schema
from pyspark.sql.types import *
schm=StructType([StructField("col_1",StringType(),True),StructField("col_2",StringType(),True),StructField("col_3",StringType(),True)])
df=spark.read.option("mode","DROPMALFORMED").csv('input2.csv',header=True,schema=schm)
df.show()

col_1 col_2   col_3
101   Murugan Healthcare
102   Kannan  Finance
103   Mani    IT
104   Pavan   HR

============================================================

19. How Spark handles the slow and long running task in your Spark application?
i.e. Speculative Execution with Demo

Task1 >>>> Completed
Task2 >>>> Completed
Task3 > Pending
Task4 >>>> Completed

The task which is consuming more time to execute will be identified by the Spark and instead of killing it, it will start one more similar task in the another worker node and when any one them finishes execution, other one will be gracefully terminated

Configs required to enable the Speculative execution, these are passed during spark-submit or in the configurations of the Spark itself, by default Spaeculative execution is false in Spark:
spark.speculation ##Manually needs to be enabled
spark.speculation.interval ##What is interval to scan each job to identify whether it is a speculative job
spark.speculation.multiplier ##This needs to be >= 1, it is a median if completed task is greater than this median in comparison to pending task, to initiate the speculative execution mode
spark.speculation.quantile ##It is a percentile of completed jobs, so out of 4 jobs in below example, 3 are completed and 1 is pending

spark.speculation=True
spark.speculation.interval=200
spark.speculation.multiplier=5
spark.speculation.quantile=0.75 ##(3/4 = 0.75)

Total task - 4
Completed task(3) - 3ms
Pending task(1) - 2s

============================================================

20. From the given CSV file, calculate Expiry date as shown in output DataFrame by adding Rechargeabledate column with Remaining days column:

RechargeId  Rechargedate    Remaining_days  validity
R201623     20200511        1               online
R201873     20200119        110             online
R201999     20200105        35              online
R201951     20191105        215             online

RechargeID: string
Rechargedate: integer
Remaining_days: integer
validity: string

RechargeId  Rechargedate    Remaining_days  validity    Expiry_date
R0201623     20200511        1               online      2020-05-12
R0201873     20200119        110             online      2020-05-08
R0201999     20200105        35              online      2020-02-09
R0201951     20191105        215             online      2020-06-07

RechargeID: string
Rechargedate: integer
Remaining_days: integer
validity: string
Expiry_date: date

import findspark
findspark.init()

from pyspark.sql import SparkSession
spark=SparkSession.builder.master("local").appName("date duration demo").getOrCreate()
in_data=spark.read.option("header","true").option("inferSchema","true").csv("input_file")
in_data.printSchema()

##Let's check all the available options with respect to Date
date_add
date_format
date_sub
date_trunc
datediff
dayofmonth
dayofweek
dayofyear
##For conversion, we can use
to_date
to_json
to_utc_timestamp
toDegrees
toRadians

from pyspark.sql.functions import date_add,to_date,col,expr
in_data.select(to_date("Rechargedate"))
Py4JJavaError: cannot cast int to date
##We have to perform casting to overcome the issue

df=in_data.select(to_date(col("Rechargedate").cast("string")))
df.show()
##This will print the data under Rechargedate column as "null", it's not performing exact conversion because it is not finding format to do the needful, let's add it
Rechargedate
null
null
null
null

df=in_data.select(to_date(col(Rechargedate).cast("string")."yyyyMMdd"))
df.show()
Rechargedate
2020-05-11
2020-01-19
2020-01-05
2019-11-05

##Let's give a name to above col as date_s and add to main table
in_date_s=in_data.withColumn("date_s",to_date(col(Rechargedate).cast("string")."yyyyMMdd"))
in_date_s.show()
RechargeId  Rechargedate    Remaining_days  validity    date_s
R201623     20200511        1               online   2020-05-11   
R201873     20200119        110             online   2020-01-19
R201999     20200105        35              online   2020-01-05
R201951     20191105        215             online   2019-11-05

##Let's add the date_s to Remaining_days, to do this we need to use expr
in_date_s.select("*",expr("date_add(date_s,Remaining_days)")).show()

RechargeId  Rechargedate    Remaining_days  validity    Expiry_date
R0201623     20200511        1               online      2020-05-12
R0201873     20200119        110             online      2020-05-08
R0201999     20200105        35              online      2020-02-09
R0201951     20191105        215             online      2020-06-07

============================================================

21. Guess Output - Coalesce():

df.rdd.getNumPartitions()
Out[]:10

Question1:
df_col=df.coalesce(4)
df_col.rdd.getNumPartitions()
Out[]: 4

Question2:
df_col=df.coalesce(15)
df_col.rdd.getNumPartitions()
Out[]: 10   ##coalesce used only for decreasing, but when we tried to increase it will not perform anything, instead the partition still remains as 10

============================================================

22. Which one returns result Faster?

##First Method is the Winner
Df=spark.read.csv("dummy")
Df1=Df.filter("x")
Df2=Df1.sort("y")
Df2.count()
##Time : 12.81s

Df=spark.read.csv("dummy")
Df1=Df.sort("y")
Df2=Df1.filter("x")
Df2.count()
##Time : 13.96s

##Below two codes were caching happens, it's evident that Spark takes some time to load data to memory
Df=spark.read.csv("dummy")
Df.cache()
Df1=Df.filter("x")
Df2=Df1.sort("y")
Df2.count()
##Time : 15.21s

Df=spark.read.csv("dummy")
Df.cache()
Df1=Df.sort("y")
Df2=Df1.filter("x")
Df2.count()
##Time : 15.83s

============================================================

23. Task is to convert the RDD to DF and DF to RDD, whether the RDD will be same as the initial stage?

Question1:
Syntax to convert RDD to Dataframe?
Syntax[]: .toDF() ##Refer below example for code

Question2:
Syntax to convert Dataframe back to RDD?
Syntax[]: .rdd

import finspark
findspark.init()

from pyspark.sql import SparkSession,types
spark=SparkSession.builder.master("local").appName("rddtodf").getOrCreate()
sc=spark.sparkContext
input_list=[['azar'],['raj'],['kamal']]
rdd1=sc.parallelize(input_list)
type(rdd1) ##pyspark.rdd.RDD
rdd1.collect() ##[['azar'],['raj'],['kamal']]

##Convert RDD to DF (approach1):
df1=rdd1.toDF()
type(df1) ##pyspark.sql.dataframe.DataFrame
df1.show()

##Convert RDD to DF (approach2):
df1=rdd.createDataFrame(rdd1,['name'])
type(df1) ##pyspark.sql.dataframe.DataFrame
df1.show()
name
azar
raj
kamal

##Convert DF to RDD
rdd2=df1.rdd
type(rdd2) ##pyspark.rdd.RDD
rdd2.collect() ##[Row(name='azar'),Row(name='raj'),Row(name='kamal')]

*******Conclusion : Nope, the RDD will not be same as the initial stage, above example is evident initially it was list, post conversion and converting back it is not a list instead it gave output in Row format

============================================================

24. Consider a file with a column Education, which has array of elements as shown below. Convert each element in the array to record using Spark Dataframe?
##Explode vs Posexplode

****Note: Take care of empty values in the array field as well

Input:
Name|Age|Education
Azar|25|MBA,BE,HSC
Har|32|
Kumar|35|ME,BE,Diploma

Output:
Name    Age Index   Qualification
Azar    25  0       MBA
Azar    25` 1       BE
Azar    25  2       HSC
Hari    32  null    null
Kumar   35  0       ME
Kumar   35  1       BE
Kumar   35  2       Diploma

import findspark
findspark.init()

#Create SparkSession and import all required packages:
from pyspark.sql import SparkSession,types
spark=SparkSession.builder.master("local").appName("scenario Based").getOrCreate()
sc=spark.sparkContext
in_df=spark.read.option("delimiter","|").csv("input_file",header=True)
in_df.show()
Name    Age Education
Azar    25  MBA,BE,HSC
Hari    32  null
Kumar   35  ME,BE,Diploma

##We need to explode Education to extract some sense of it, but to explode the data under column 'Education' needs to be of map,array and struct type, but in our case it is a string, therefore we need to use split before using explode

from pyspark.sql.functions import explode,split
in_df.withColumn("Qualification",explode(split("Education",","))).show()
##Records are exploded, seems like null value is missing
Name    Age Education       Qualification
Azar    25  MBA,BE,HSC      MBA
Azar    25  MBA,BE,HSC      BE
Azar    25  MBA,BE,HSC      HSC
Kumar   35  ME,BE,Diploma   ME
Kumar   35  ME,BE,Diploma   BE
Kumar   35  ME,BE,Diploma   Diploma

##To get null value as in the output we can go for explode_outer
from pyspark.sql.functions import explode_outer,split
in_df.withColumn("Qualification",explode_outer(split("Education",","))).show()

Name    Age Education       Qualification
Azar    25  MBA,BE,HSC      MBA
Azar    25  MBA,BE,HSC      BE
Azar    25  MBA,BE,HSC      HSC
Hari    32  null            null
Kumar   35  ME,BE,Diploma   ME
Kumar   35  ME,BE,Diploma   BE
Kumar   35  ME,BE,Diploma   Diploma

##We need to use posexplode we have to go with select statement, this will give us the positio of the index in an array
from pyspark.sql.functions import posexplode_outer
in_df.select("*",posexplode_outer(split("Education",","))).show()

Name    Age Education       Col     Pos
Azar    25  MBA,BE,HSC      MBA     0
Azar    25  MBA,BE,HSC      BE      1
Azar    25  MBA,BE,HSC      HSC     2
Hari    32  null            null    null
Kumar   35  ME,BE,Diploma   ME      0
Kumar   35  ME,BE,Diploma   BE      1
Kumar   35  ME,BE,Diploma   Diploma 2

##For renaming the column:
in_df.select("*",posexplode_outer(split("Education",","))).withColumnRenamed("Col","Qualification").withColumnRenamed("pos","Index").show()

Name    Age Education       Qualification  Index
Azar    25  MBA,BE,HSC      MBA            0
Azar    25  MBA,BE,HSC      BE             1
Azar    25  MBA,BE,HSC      HSC            2
Hari    32  null            null           null
Kumar   35  ME,BE,Diploma   ME             0
Kumar   35  ME,BE,Diploma   BE             1
Kumar   35  ME,BE,Diploma   Diploma        2

##For dropping a non-required column:
in_df.select("*",posexplode_outer(split("Education",","))).withColumnRenamed("Col","Qualification").withColumnRenamed("pos","Index").drop("Education").show()

Name    Age Qualification Index
Azar    25  MBA           0
Azar    25  BE            1
Azar    25  HSC           2
Hari    32  null          null
Kumar   35  ME            0
Kumar   35  BE            1
Kumar   35  Diploma       2

============================================================

25. How to handle the Skewness of Data in Spark?
##FYI : What is Skewness??
Non uniform distribution of data across the partition in cluster is called Skewness
Issues due to Skewness:
-Long running Task, job gets stuck on last stage. i.e., 199/200 completed
-Hampers the benefit of parallelism and leads to degaradation of performance
-Inconsistency in processing time
##To overcome Skewness, in Spark 3.0 we have a feature called as Adaptive Query Execution, basically what it does is consider there are 5 partition, out of 5 partitions 1st Partition has the highest data, during Adaptive query execution 1st Partition will be divided into 1a and 1b and it will be executed, therefore the data size is reduced and post which joining or transformation on it becomes easy

##Talking about 2.0 version we have below options
-Repartition : Not so effective if single partition dominant column is present means
-Salting Technique : Similar to Adaptive Query Execution, a random number will be added to partition and end result will be another partition like (A with 23) >> A23,(A with 25) >> A25
-Reduce data skew effect before uploading : By opting for any other column for partition or try any way to manipulate the data to reduce skewness
-Bump up spark.sql.autoBroadcastJoinThreshold : This can be done in the Spark Config, this will help increasing likeliwood of Spark engine to choose the Broadcast Join in the Sort Merge Join, helps in avoiding Skewness of Data
-Iterative(Chunked) Broadcast Join : Comparitively larger data is sliced into smaller chunks and this chunk is again broadcasted to join with the huge volume of the data, post which all the data is union to single dataset with the help of this we will be able to overcome the skewness

============================================================

26. Consider we have a datafile of students mark list, we need to transpose subject column and calculate total marks for each student as shown below

ROLL_NO|SUBJECT|MARKS
1001|English|84
1001|Physics|55
:
:

ROLL_NO English History Maths Physics Total
1002    84      32.............       352
1001    84      78..............      251

***Note: We can achieve this using Pivot function:

import findspark
findspark.init()

from pyspark.sql import SparkSession
spark=SparkSession.builder.master("local").appName("pivot").getOrCreate()

df_in=spark.read.option("delimiter","|").option("inferSchema","True").csv("input file")
df_in.show()
df_in.printSchema()

ROLL_NO SUBJECT MARKS
1001    English 84
:
:

root
|-- ROLL_NO: integer (nullable=true)
|-- SUBJECT: string (nullable=true)
|-- MARKS: integer (nullable=true)

###Note: To perform pivoting we need atleast one numerical column

tbl1=df_in.groupby("ROLL_NO").pivot("SUBJECT").max("MARKS")
tbl1.show()

ROLL_NO English History Maths Physics
1002    84      32.............      
1001    84      78..............     

##To find the total of subjects, we can achieve it by two methods,
-By adding the subjects
-By joining the two dataframes
Let's go by adding the subjects

tbl1.withColumn("Total",tbl1['English']+tbl1['Science']+tbl1['Physics']+tbl1['Maths']+tbl1['History']).show()

ROLL_NO English History Maths Physics Total
1002    84      32.............       352
1001    84      78..............      251

============================================================

27. To merge the two complex Spark dataframe with different schema into single dataframe as shown in the diagram

input1.json: 
[{"name":"AZAR","Education":{"Qualification":"BCOM","year":2013,"Age":28}},
{"name":"CHIN","Education":{"Qualification":"BE","year":2010,"Age":35}},
]

root
|-- Education: struct (nullable=true)
|   |-- Age: long (nullable=true)
|   |-- Qualification: string (nullable=true)
|   |-- year: long (nullable=true)
|-- name: string (nullable=true)

input2.json:
[{"name":"Clarke","Education":{"Qualification":"BCOM","year":2013}},
{"name":"Michael","Education":{"Qualification":"BE","year":2010}},
]

root
|-- Education: struct (nullable=true)
|   |-- Qualification: string (nullable=true)
|   |-- year: long (nullable=true)
|-- name: string(nullable=true)

output:
Education       name
[,BE,2011]      Clarke
[,BE,2010]      Michael
[28,BCOM,2013]  AZAR

root
|-- Education: struct (nullable=true)
|   |-- Age: long (nullable=true)
|   |-- Qualification: string (nullable=true)
|   |-- year: long (nullable=true)
|-- name: string (nullable=true)

import findspark
findspark.init()

from pyspark.sql import SparkSession

spark=SparkSession.builder.master("local").appName("Complex DataType").getOrCreate

input_df=spark.read.json("input1.json",multiline=True)
input_df.printSchema()
input_df1=spark.read.json("input2.json",multiline=True)
input_df1.printSchema()
input_df.schema ##Gives indepth details of Struct
input_df1.schema ##Gives indepth details of Struct

from pyspark.sql.types import *
from pyspark.sql.functions import col.lit,struct

##Below function helps in breaking/flattening the struct values
def flatten_struct(schema, prefix=""):
    result=[]
    for elem in schema:
        if isinstance(elem.dataType, StructType):
            result+=flatten_struct(elem.dataType,prefix + elem.namea+".")
        #result+replace("column")
        else:
            result.append(col(prefix+elem.name).alias(prefix+elem.name))
    return result
l1=flatten_struct(input_df.schema)
l2=flatten_struct(input_df1.schema)

##Will give the flattened columns list
l1
l2

list1=[]
list2=[]
for i in l1:
    list1.append(str(i).split("'")[1])
for i in l2:
    list2.append(str(i)).split("'")[1])
    
list1
list2

chk=set(list2)+set(list1)
for i in chk:
    if i.find("."):
        colm=i.split(".")[0]
        colm_new=i.split(".")[1]
        s_fields=input_df.schema[colm].dataType.names
        s_type=input_df1.schema[colm].dataType[colm_new].dataType
        in_df=input_df.withColumn(colm,struct(*([col(colm)[c].alias(c) for c in s_fields] + [lit("null").cast(s_type).alias(colm_new)])))
        s_fields=sorted(in_df.schema[colm].dataType.names)
        in_df=in_df.withColumn(colm,struct(*([col(colm)[c].alias(c) for c in s_fields])))
in_df.printSchema()
out_df=in_df.union(input_df1)
out_df.show()
Education       name
[,BE,2011]      Clarke
[,BE,2010]      Michael
[28,BCOM,2013]  AZAR

=============================================================

28. Consider we have a CSV with a column request having JSON like data in it. How will you flatten the JSON format string column into a separate columns shown in the output dataframe:

input:
PartitionDate	Status	        request
2020-06-30	    Internal Error	{"Response":{"MessageId" : 15432 }}
2020-06-30	    Success	        {"Response":{"MessageId" : 15432,"Latitude":"-176.2989","longitude":"7.3614" }}

root
|-- PartitionDate: string (nullable=true)
|-- Status: string (nullable=true)
|-- request: integer (nullable=true)

output:
PartitionDate   Status          Latitude    MessageId   Longitude
2020-06-30      Internal Error  null        15432       null
2020-06-30      Success         -176.2989   15432       7.3614

root
|-- PartitionDate: string (nullable=true)
|-- Status: string (nullable=true)
|-- Latitude: string (nullable=true)
|-- MessageId: long (nullable=true)
|-- Longitude: string (nullable=true)


import findspark
findspark.init()

#Create SparkSession and import all required packages
from pyspark.sql import SparkSession,types

spark=SparkSession.builder.master("local").appName('Json Complex').getOrCreate()

inp=spark.read.option("header",True).option("escape","\"").option("multiline","true").csv("input_file")

inp.printSchema()

from pyspark.sql.functions import col,json_tuple,to_json,from_json

##Method 1: Using JSON tuple

##inp.select("*",json_tuple("request","Response")).show()

inp.select("*",json_tuple("request","Response")).drop("request").select("*",json_tuple("c0","MessageId","Latitude","longitude").alias("MessageId","Latitude","longitude")).drop("c0").show()

#Note: Json tuple is case sensitive, better to use same naming convention

##Method 2: Using From_Json, helps in iterating through columns

inp.select(col('request').alias("jsoncol")).rdd.map(lambda x: x.jsoncol)
in_sch=spark.read.json()inp.select(col('request').alias("jsoncol").rdd.map(lambda x: x.jsoncol)).schema

in_sch ##Will printschema, all the data will be in StructType/StructField concept

inp_json=inp.select("*",from_json("request",in_sch).alias("jsonstr"))

inp_json.printSchema()

col1=inp_json.schema['jsonstr'].dataType.names[0]
chk="jsonstr."+col1+".*"

inp_json.select("*",col(chk)).drop("request","jsonstr").show()

##Method 3: Usage of to_json:
inp_json.select(col("jsonstr.*")).select(to_json(col("Response"))).show()
##It's a work from home

=============================================================

29. Spark Optimization concept while reading a Schema of the given file
-Without inferschema >> 2 Jobs are created, 1 is for Spark Job(Which reads through file to get only header) and other one is to create a dataframe, this takes time
-With inferSchema >> 2 Jobs are created, 1 is for Spark Job(Which reads through file the completely to understand the schema) and other one is to create a dataframe, this takes time more than without inferSchema
-Predefined Schema to using StructType: Here no Spark job is triggered, through pre-defined schema appropriate datatypes are defined, also time taken is very less

##Note: Always advisable to use pre-defined schema, if inferschema needs to be used, then on Day1 trigger to read it, save it to any of the Lookup files, from Day2 onwards read from Lookup file

=============================================================

30. Consider a Spark Dataframe as shown in input with an ambiguous column (also called as duplicate column) named "name", How will you rename any one of the ambiguous column as shown in dataframe

input_json file:
[{"name":"AZAR",
  "product":"Headphone",
  "Delivery":{
      "name":"Azarudeen",
      "address":"Chennai",
      "mob":"1234567"}},
{"name":"Bharath",
  "product":"T-shirt",
  "Delivery":{
      "name":"Bharathiraj",
      "address":"Bangalore",
      "mob":"5738612"}}
]

input_dataframe:
name product .....name

output_dataframe:
name_0 product .....name

Step1: 

#Read the input json file and flatten the data to replicate the use-case
df=spark.read.json('input1.json',multiLine=True)
df1=df.select("*","Delivery.*").drop("Delivery")
df1.show()

lst=[]
df_cols=df1.columns

for i in df_cols:
    if df_cols.count(i)==2:
        ind=df_cols.index(i)
        lst.append(ind)
lst1=list(set(lst))
for i in lst1:
    df_cols[i]=df_cols[i]+'_0'

df1=df1.toDF(*df_cols)
df1.show()

=============================================================

31. Consider we have two Spark Dataframe as shown above, what is the best approach:
-To find the common records in both file1 and file2?
-To find records available in File1 and not in File2?

File1:
======
Roll_no Student_name    Mobile
1001    Akash           123456
1006    Magesh          987456

File2:
======
Roll_no Student_name    Mobile
1001    Akash           123456

Out_df1:
========
Roll_no Student_name    Mobile
1001    Akash           123456

Out_df2:
========
Roll_no Student_name    Mobile
1001    Magesh          987456

from findspark
findspark.init()

from pyspark.sql import SparkSession
spark=SparkSession.builder.appName("Set Operation").get)rCreate()
master_df=spark.read.option("delimiter","|").csv("input_file1",header=True)
daily_df=spark.read.option("delimiter","|").csv("input_file2",header=True)

master_df.show()
daily_df.show()

Set Operators and Joins:
##Set Operators
-union -unionAll -distinct -intersect -intersectAll -subtract -exceptAll
##Joins
-inner -outer -leftouter -rightouter -leftsemi -leftanti -cartesian etc.,

##Question1: To find common records between two DFs
master_df.intersect(daily_df).show() ##Provides unique records
master_df.intersectAll(daily_df).show() ##Includes duplicates as well (|||lr to union all)
master_df.join(daily_df,on=["Roll_no","Student_name","Mobile"],home="leftsemi").show()

##Note: In general both the Set Operators and Joins internally call Brocast hashjoin, moreover the Set Operators again call the Joins internally, Sick!! We can directly use joins, but syntax of set operators seems simple(#of columns needs to be same for intersect |||lr to union/unionAll, i.e. the challenge), performance wise both are same

##Question2: To find records presnt in File1 and not in File2
master_df.subtract(daily_df).show() ##Provides unique records
master_df.exceptAll(daily_df).show() ##Includes duplicates as well (|||lr to union all)
master_df.join(daily_df,on=["Roll_no","Student_name","Mobile"],how="leftanti").show()

=============================================================

32. Consider an input file with some dummy rows [row no. 0 to 6] before actual data as shown in input. How will you remove those dummy lines and load the data into Spark DF as shown in output DF:

##Create SparkSession and SparkContext as in below snippet

from pyspark.sql import SparkSession
spark=SparkSession.builder.master("local").appName("Remove N lines").getOrCreate()
sc = spark.sparkContext

##Read the file as RDD. Here we are reading with the partition as 2. Refer code snippet

inp=sc.textFile("pageview.csv",2).map(lambda x: x.split(','))
##Map works on row by row basis
inp.getNumPartitions()
inp.collect()

rdd_drop=inp.mapPartitionsWithIndex(lambda id_x, iter: list(iter)[8:] if(id_x == 0) else iter)
rdd_drop.collect()
##MapPartitionsWithIndex works on each partition and applies logic on each index
schema=['Page','Date','Pageviews','unique_views','session']
out_df=spark.createDataFrame(rdd_drop,schema)
out_df.show(10,truncate=0)

