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
- Module 3 - Programming Hadoop with Pig
- Module 4 - Programming Hadoop with Spark
- Module 5 - Using relational data stores with Hadoop
- Module 6 - Using non-relational data stores with Hadoop