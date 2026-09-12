## CSV File Creation Rules

Before importing a CSV file, make sure to follow these rules:

### 1. Create the file from the terminal

```bash
code name.csv
```

### 2. Write the column names in the first row

The first row must contain the column names, separated **only by commas**, with no spaces or any other characters in between.

**Correct:**
```
name,age,city
```

**Incorrect (separated by spaces):**
```
name age city
```

**Incorrect (extra space after commas):**
```
name, age, city
```

### 3. Why does this matter?

Python's `csv.DictReader` and `csv.DictWriter` methods use **comma as the default delimiter**.

- **If spaces are used instead of commas:** The entire line is read as a single column, and the data cannot be parsed. The code will not work.
- **If there are extra spaces after the commas:** The file will still be read, but the column names will contain hidden leading spaces (e.g. `" age"` instead of `"age"`). This can cause a `KeyError` when accessing `row["age"]` in your code.
