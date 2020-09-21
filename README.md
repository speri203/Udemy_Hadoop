# U-demy Hadoop

Created: Sep 16, 2020 9:45 PM
Reviewed: No
Subject: Hadoop, U-Demy

- Module 1 - Learn all the buzzwords! And Install the Hortonworks Data Platform Sandbox
    - The framework used in this course is the 'Hortonworks Data Platform"
        - Download link: [https://www.cloudera.com/downloads/hortonworks-sandbox/hdp.html](https://www.cloudera.com/downloads/hortonworks-sandbox/hdp.html)
        - Version HDP 2.6.5
        - VirtualBox: [https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads)
    - Technologies included
        - Hive: Allows SQL execution on Hadoop cluster. Allows data to be presented in SQL database format. Can be though of as a database.
        - HBase: This is a NoSQL database. Fast way to interact with transactional platform.
        - Spark: Lets you interact with data using a several different languages. Allows machine learning across clusters and several other cool features.
        - Flume: Transfers web logs at a large scale to your cluster.
        - Oozie: Job scheduler.
        - Ambari: This technology allows us to interact with the Hadoop cluster through a web browser. The alternative is using SSH to connect to the machine.
        - MongoDB:
        - Cassandra:
        - Kafka: General purpose log collector from your nodes.
        - Storm
        - Pig: High level programming API that lets you write simple scripts that look a lot like SQL. Alleviates the need to write Python or Java code.
        - Tez: Used in conjunction with Hive accelerate it. Lets you optimize queries.
        - Drill: Write SQL queries that will work on a variety of NoSQL DB.
        - Pheonix: Similar to Drill. With the added bonus as ACID guarantee
        - Hue:
        - Mesos: An alternative to YARN. Used to manage resources.
        - YARN: Yet another resource negotiator, the system that manages the resources on a cluster.
        - MapReduce: Programming module that lets you process data across clusters. Consists of Mappers and Reducers.
            - Mappers: transform your data in parallel across your whole cluster.
            - Reducers: Aggregates the data together.
        - MySQL: Relational DB
        - Presto: Execute queries across clusters.
        - Sqoop: Ties your Hadoop database into a relational database. Can be thought of a connector.
        - Zeppelin
        - Zookeeper: Technology to coordinate everything on your cluster.
        - Storm: Processing streaming data. Useful when using sensor data and this can be done in real-time.
        - HDFS: Hadoop distributed file system, this allows us to distribute the storage of big data across clusters. Also maintains redundant copies.
    - The Hortonworks sandbox saves a lot of time by setting up the Hadoop environment with all the dependencies. The file is quite large and the VM settings use 4 cores with 8 gb of RAM. The OS this environment uses is CentOS
    - The data for this course can be downloaded from grouplens. This is a dataset of movie ratings
        - link: [https://grouplens.org/datasets/movielens/](https://grouplens.org/datasets/movielens/)
    - The movie 100k dataset consists of the following headers
        - User ID
        - Movie ID (can refer to u.item to identify which movies ids correspond to)
        - Rating
        - Timestamp
    - Tables can be uploaded using the "Hive View" functionality in Ambari sandbox
    - Once tables have been created/uploaded queries can be run on them using the 'Query' tab
    - Hadoop: An open source software platform from distributed storage and distributed processing of very large datasets on computer clusters built from commodity hardware.
    - Why Hadoop?
        - Data's too big - terabytes per day
        - Vertical scaling doesn't cut it
        - Horizontal scaling is linear
        - Not just for batch processing anymore
- Module 2 - Using Hadoop's Core: HDFS and MapReduce
    - HDFS: Hadoop distributed file system
        - Handles big files
        - Accomplishes this by breaking up the data into 128mb blocks
        - Allows distributing of processing by allocating these blocks onto many machines
        - Can be stored across many computers. More than one copy is stored to deal with failure of drives
    - HDFS Architecture
        - Name Node: Keeps track of where all the blocks are allocated to. Also maintains an edit log that keeps track of what is being created/modified/delete etc.
        - Data Node:  Where blocks of data are stored

            ![U-demy%20Hadoop%2068a5d32e703c42a8947174e9a5405439/Capture.png](U-demy%20Hadoop%2068a5d32e703c42a8947174e9a5405439/Capture.png)

            ![U-demy%20Hadoop%2068a5d32e703c42a8947174e9a5405439/writing_file.png](U-demy%20Hadoop%2068a5d32e703c42a8947174e9a5405439/writing_file.png)

        - Only one name node is active at a time. These are methods used in case the name node goes offline to retain data
            - Back up metadata: Namenode writes to local disk and NFS
            - Secondary Namenode: Maintains merged copy of the edit log can restore from
            - HDFS Federation: Each namenode manages a specific namespace volume
            - HDFS High Availability
                - Hot standby namenode using shared edit log
                - Zookeeper tracks active namenodes
                - Uses extreme measures to ensure only one namenode is used at a time
            - Using HDFS
                - UI (Ambari)
                - Command-line interface
                - HTTP / HDFS proxies
                - Java Interface
                - NFS Gateway
        - 'File view' gives you the functionality of interacting with the node like a file explorer. You are able to navigate to user and create, delete, copy, move, concatenate, etc directories on the HDFS.
        - Within the HDFS tab on the left you are able to see how many namenodes, datanodes, space used and so on.
        - To interact with the Hadoop system using command line you have to prefix the command with the hadoop keyword

            ```bash
            hadoop fs -ls 
            hadoop fs -mkdir [dir_name]
            hadoop fs -copyFromLocal [filename] [relativepath]
            hadoop fs -rm [relativepath]
            hadoop fs -rmdir [relativepath]
            hadoop fs -help
            ```

        - Why MapReduce?
            - Distributes the processing of data on your cluster
            - Divides your data up into partitions that are **MAPPED** (transformed) and **REDUCED** (aggregated) by mapper and reducer functions you define.
            - Resilient to failure - an application master monitors your mappers and reducers on each partition.
        - From the Mapper function the result is a key:value pair

            ![U-demy%20Hadoop%2068a5d32e703c42a8947174e9a5405439/mapper.png](U-demy%20Hadoop%2068a5d32e703c42a8947174e9a5405439/mapper.png)

        - The next step is that MapReduce will automatically aggregate the values and sort them. This is called Mapped Data (Shuffle and Sort) **The Shuffle and Sort stage sorts by the key.**

            ![U-demy%20Hadoop%2068a5d32e703c42a8947174e9a5405439/mapped_data.png](U-demy%20Hadoop%2068a5d32e703c42a8947174e9a5405439/mapped_data.png)

        - Reducer: Decides what to do with the output

            ![U-demy%20Hadoop%2068a5d32e703c42a8947174e9a5405439/reducer.png](U-demy%20Hadoop%2068a5d32e703c42a8947174e9a5405439/reducer.png)

        - The final pipeline for the above will look like this

            ![U-demy%20Hadoop%2068a5d32e703c42a8947174e9a5405439/full_pipeline.png](U-demy%20Hadoop%2068a5d32e703c42a8947174e9a5405439/full_pipeline.png)

        - The overall pipeline of how HDFS handles MapReduce

            ![U-demy%20Hadoop%2068a5d32e703c42a8947174e9a5405439/hdfs_map_reduce.png](U-demy%20Hadoop%2068a5d32e703c42a8947174e9a5405439/hdfs_map_reduce.png)

        - MapReduce is natively Java
        - **STREAMING** allows interfacing to other languages (Python)
        - Application master monitoring worker tasks for errors or hanging
            - Restarts as needed
            - Preferably on a different node
        - What if the application master goes down?
            - YARN can try to restart it
        - What if an entire Node goes down?
            - This could be an application master
            - The resource manager will try to restart it
        - What if the resource monitor goes down?
            - Can set up "high availability" (HA) using Zookeeper to have a hot standby
        - Problem: Count the number of reviews for each rating
            - MAP each input line to (rating, 1)
            - REDUCE each rating with the sum of all the 1's

            ![U-demy%20Hadoop%2068a5d32e703c42a8947174e9a5405439/problem1.png](U-demy%20Hadoop%2068a5d32e703c42a8947174e9a5405439/problem1.png)

        - The following should be run on the Hortonworks VM in-order to get MapReduce working.

            ```bash
            ## pip
            yum install python-pip
            ## MRJob
            pip install mrjob==0.5.11
            ## Nano or neovim
            yum install nano
            yum install nvim
            ## Data files and the script
            wget http://media.sundog-soft.com/hadoop/ml-100k/u.data
            wget http://media.sundog-soft.com/hadoop/RatingsBreakdown.py
            ```

        - Running the python script to run the MapReduce functionality

            ```bash
            ## Run Locally
            python RatingsBreakdown.py u.data
            ## Run with hadoop
            python RatingsBreakdown.py -r hadoop --hadoop-streaming-jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar u.data
            ```

- Module 3 - Programming Hadoop with Pig
- Module 4 - Programming Hadoop with Spark
- Module 5 - Using relational data stores with Hadoop
- Module 6 - Using non-relational data stores with Hadoop