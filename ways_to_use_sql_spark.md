# Ways to Use SQL in PySpark

## Methods

### Temporary View
* Create a temporary view from a DataFrame.
* Use `createOrReplaceTempView()` method.
* Query using `spark.sql()`.

### Global Temporary View
* Create a global temporary view from a DataFrame.
* Use `createOrReplaceGlobalTempView()` method.
* Query using `spark.sql()`.

### Permanent View
* Create a permanent view from a DataFrame.
* Use `saveAsTable()` method.
* Query using `spark.sql()`.

### DataFrames' `sql` method
* Use `sql()` method on a DataFrame.
* No need to create a view.

### `SparkSession`'s `sql` method
* Register DataFrame as table.
* Use `spark.sql()`.

### DataFrames' `select` and `filter` methods
* Use DataFrame API instead of SQL.
* No need to create a view.

### DataFrames' `queryExecution` method
* Execute query directly on DataFrame.
* No need to create a view.

## Comparison Chart

| Method                   | Complexity | Performance | Readability | Persistence | Sharing |
| :----------------------- | :--------- | :---------- | :---------- | :---------- | :------ |
| Temporary View           | Low        | Good        | Good        | Session     | No      |
| Global Temporary View    | Low        | Good        | Good        | Session     | Yes     |
| Permanent View           | Medium     | Good        | Good        | Permanent   | Yes     |
| DataFrames' sql          | Medium     | Good        | Fair        | No          | No      |
| SparkSession's sql       | Medium     | Good        | Fair        | No          | Yes     |
| DataFrames' select/filter | Low        | Excellent   | Excellent   | No          | No      |
| DataFrames' queryExecution | High       | Excellent   | Poor        | No          | No      |

## Best Method: DataFrames' `select` and `filter` methods

### Reasons:
* **Performance:** DataFrame API is optimized for performance.
* **Readability:** Code is more readable and maintainable.
* **Simplicity:** No need to create views or register tables.
* **Flexibility:** Supports complex queries and operations.

### When to use other methods:
* **Temporary View:** Simple queries, testing, and development.
* **Global Temporary View:** Sharing data between sessions.
* **Permanent View:** Production, sharing data across cluster.
* **DataFrames' sql:** Complex queries, SQL-specific features.
* **SparkSession's sql:** Sharing data between sessions.