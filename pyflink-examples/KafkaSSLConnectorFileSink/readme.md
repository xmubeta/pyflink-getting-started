# kafka SSL connector for pyflink

Flink version - 1.15.2

Required libraries to add
* flink-connector-kafka-1.15.2.jar ,
* kafka-clients-3.3.1.jar
* com.amazonaws.msk-config-providers-0.2.0-all.jar

To adapt to running on Amazon Managed Apache Flink, generate a UBER jar (lib/FatJarMaker-1.0-SNAPSHOT-combined.jar) with these three jars.

To connect to Kafka with SSL keystore and truststore, use Apache Kafka Config Providers (https://github.com/aws-samples/msk-config-providers )
Set up Secrets Manage to store password of keystore and truststore, then put keystore and truststore files on S3.

This example demonstrates 
* How to consume & produce records using pyflink SQL connector for kafka with SSL certificates. 
* Write to Amazon S3

