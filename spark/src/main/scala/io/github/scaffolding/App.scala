package io.github.scaffolding

import org.apache.log4j.{Level, Logger}

import org.apache.spark.sql.SparkSession

/**
  * Hello world!
  *
  */
object Main {

  def main(args: Array[String]): Unit = {

    //参数检查
    if (args.length < 2) {
      System.err.println("Usage: MyScalaWordCout <input> <output> ")
      System.exit(1)
    }
    //获取参数
    val input = args(0)
    val output = args(1)

    val spark = SparkSession
      .builder()
      .master("local[2]")
      .appName("Spark Demo")
      .config("hive.metastore.uris", "thrift://localhost:9083")
      .enableHiveSupport()
      .getOrCreate()

    spark.sparkContext.setLogLevel("ERROR")

    spark.sql("use yc_bit")
    spark.sql("show tables").show()

    spark.sql("select dt, count(1) from yc_bit.fo_service_order group by dt order by dt").show()

    spark.stop()
  }

}
