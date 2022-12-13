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
