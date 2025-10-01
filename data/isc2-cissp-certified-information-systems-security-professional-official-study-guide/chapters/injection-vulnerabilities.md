---
{
  "id": "chapter-233",
  "title": "Injection Vulnerabilities",
  "order": 233,
  "source": {
    "href": "c21.xhtml",
    "anchor": "head-2-369"
  },
  "est_tokens": 2710,
  "slug": "injection-vulnerabilities",
  "meta": {
    "nav_title": "Injection Vulnerabilities",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Injection Vulnerabilities

Injection vulnerabilities are among the primary mechanisms that attackers use to break through a web application and gain access to the systems supporting that application. These vulnerabilities allow an attacker to supply some type of code to the web application as input and trick the web server into either executing that code or supplying it to another server to execute.

There are a wide range of potential injection attacks. Typically, an injection attack is named after the type of back-end system it takes advantage of or the type of payload delivered (injected) onto the target. Examples include SQL injection, Lightweight Directory Access Protocol (LDAP), XML injection, command injection, HTML injection, code injection, and file injection.

### SQL Injection Attacks

Web applications often receive input from users and use it to compose a database query that provides results that are sent back to a user. For example, consider the search function on an ecommerce site. If a user enters orange tiger pillows in the search box, the web server needs to know what products in the catalog might match this search term. It might send a request to the back-end database server that looks something like this:

```

SELECT ItemName, ItemDescription, ItemPrice

FROM Products

WHERE ItemName LIKE '%orange%' AND

ItemName LIKE '%tiger%' AND

ItemName LIKE '%pillow%'
```

`SELECT ItemName, ItemDescription, ItemPrice`

`FROM Products`

`WHERE ItemName LIKE '%orange%' AND`

`ItemName LIKE '%tiger%' AND`

`ItemName LIKE '%pillow%'`

This command retrieves a list of items that can be included in the results returned to the end user. In a SQL injection attack, the attacker might send a very unusual-looking request to the web server, perhaps searching for this:

```

orange tiger pillow'; SELECT CustomerName, CreditCardNumber FROM Orders; --
```

`orange tiger pillow'; SELECT CustomerName, CreditCardNumber FROM Orders; --`

If the web server simply passes this request along to the database server, it would do this (with a little reformatting for ease of viewing):

```

SELECT ItemName, ItemDescription, ItemPrice

FROM Products

WHERE ItemName LIKE '%orange%' AND

ItemName LIKE '%tiger%' AND

ItemName LIKE '%pillow';

SELECT CustomerName, CreditCardNumber

FROM Orders;

--%'
```

`SELECT ItemName, ItemDescription, ItemPrice`

`FROM Products`

`WHERE ItemName LIKE '%orange%' AND`

`ItemName LIKE '%tiger%' AND`

`ItemName LIKE '%pillow';`

`SELECT CustomerName, CreditCardNumber`

`FROM Orders;`

`--%'`

This command, if successful, would run two different SQL queries (separated by the semicolon). The first would retrieve the product information, and the second would retrieve a listing of customer names and credit card numbers. This is just one example of using a SQL injection attack to violate confidentiality restrictions. SQL injection attacks may also be used to execute commands that modify records, drop tables, or perform other actions that violate the integrity and/or availability of databases.

In the basic SQL injection attack we just described, the attacker is able to provide input to the web application and then monitor the output of that application to see the result. Although that is the ideal situation for an attacker, many web applications with SQL injection flaws do not provide the attacker with a means to directly view the results of the attack. However, that does not mean the attack is impossible; it just makes it more difficult. Attackers use a technique called blind SQL injection to conduct an attack even when they don't have the ability to view the results directly. We'll discuss two forms of blind SQL injection: content-based and timing-based.

#### Blind Content-Based SQL Injection

In a content-based blind SQL injection attack, the perpetrator sends input to the web application that tests whether the application is interpreting injected code before attempting to carry out an attack. For example, consider a web application that asks a user to enter an account number. A simple version of this web page might look like the one shown in Figure 21.1 .

FIGURE 21.1 Account number input page

FIGURE 21.1 Account number input page

When a user enters an account number into that page, they would next see a listing of the information associated with that account, as shown in Figure 21.2 .

FIGURE 21.2 Account information page

FIGURE 21.2 Account information page

The SQL query supporting this application might be something similar to this:

```

SELECT FirstName, LastName, Balance

FROM Accounts

WHERE AccountNumber = '$account'
```

`SELECT FirstName, LastName, Balance`

`FROM Accounts`

`WHERE AccountNumber = '$account'`

where the $account field is populated from the input field in Figure 21.1 . In this scenario, an attacker could test for a standard SQL injection vulnerability by placing the following input in the account number field:

```

52019' OR 1=1;--
```

`52019' OR 1=1;--`

If successful, this would result in the following query being sent to the database:

```

SELECT FirstName, LastName, Balance

FROM Accounts

WHERE AccountNumber = '52019' OR 1=1;

--'
```

`SELECT FirstName, LastName, Balance`

`FROM Accounts`

`WHERE AccountNumber = '52019' OR 1=1;`

`--'`

This SELECT query, which includes the OR 1=1 condition, would match all results. However, the design of the web application may ignore any query results beyond the first row. If this is the case, the query would display the same results as shown in Figure 21.2 . Although the attacker may not be able to see the results of the query, that does not mean the attack was unsuccessful. However, with such a limited view into the application, it is difficult to distinguish between a well-defended application and a successful attack.

`SELECT`

`OR 1=1`

The last line of the query, --' , is ignored by the database because the -- character sequence indicates a comment that should be ignored during execution. The purpose of including it in the query is to avoid an error that might be introduced by the leftover apostrophe in the query template.

`--'`

`--`

The attacker can perform further testing by taking input that is known to produce results, such as providing the account number 52019 from Figure 21.2 and using SQL that modifies that query to return no results. For example, the attacker could provide this input to the field:

```

52019' AND 1=2;--
```

`52019' AND 1=2;--`

If the web application is vulnerable to blind SQL injection attacks, it would send the following query to the database:

```

SELECT FirstName, LastName, Balance

FROM Accounts

WHERE AccountNumber = '52019' AND 1=2;

--'
```

`SELECT FirstName, LastName, Balance`

`FROM Accounts`

`WHERE AccountNumber = '52019' AND 1=2;`

`--'`

This query, of course, never returns any results, because 1 is never equal to 2! Therefore, the web application would return a page with no results, such as the one shown in Figure 21.3 . If the attacker sees this page, they can be reasonably sure that the application is vulnerable to blind SQL injection and can then attempt more malicious queries that alter the contents of the database or perform other unwanted actions.

FIGURE 21.3 Account information page after blind SQL injection

FIGURE 21.3 Account information page after blind SQL injection

#### Blind Timing-Based SQL Injection

In addition to using the content returned by an application to assess susceptibility to blind SQL injection attacks, penetration testers may use the amount of time required to process a query as a channel for retrieving information from a database.

These attacks depend on delay mechanisms provided by different database platforms. For example, Microsoft SQL Server's Transact-SQL allows a user to specify a command such as this:

```

WAITFOR DELAY '00:00:15'
```

`WAITFOR DELAY '00:00:15'`

This would instruct the database to wait 15 seconds before performing the next action. An attacker seeking to verify whether an application is vulnerable to time-based attacks might provide the following input to the account ID field:

```

52019'; WAITFOR DELAY '00:00:15'; --
```

`52019'; WAITFOR DELAY '00:00:15'; --`

An application that immediately returns the result shown in Figure 21.2 is probably not vulnerable to timing-based attacks. However, if the application returns the result after a 15-second delay, it is likely vulnerable.

This might seem like a strange attack, but it can actually be used to extract information from the database. For example, imagine that the Accounts database table used in the previous example contains an unencrypted field named Password. An attacker could use a timing-based attack to discover the password by checking it letter by letter.

The SQL to perform a timing-based attack is a little complex and you won't need to know it for the exam. Instead, here's some pseudocode that illustrates how the attack works conceptually:

```

For each character in the password

 For each letter in the alphabet

 If the current character is equal to the current letter, wait 15

 seconds before returning results
```

`For each character in the password`

`For each letter in the alphabet`

`If the current character is equal to the current letter, wait 15`

`seconds before returning results`

In this manner, an attacker can cycle through all of the possible password combinations to ferret out the password character by character. This may seem very tedious, but security tools like SQLmap and Metasploit automate blind timing-based attacks, making them quite straightforward.

### Code Injection Attacks

SQL injection attacks are a specific example of a general class of attacks known as code injection attacks. These attacks seek to insert attacker-written code into the legitimate code created by a web application developer. Any environment that inserts user-supplied input into code written by an application developer may be vulnerable to a code injection attack.

Similar attacks may take place against other environments. For example, attackers might embed commands in text being sent as part of a Lightweight Directory Access Protocol (LDAP) query, conducting a LDAP injection attack . In this type of injection attack, the focus of the attack is on the back end of an LDAP directory service rather than a database server. If a web server front end uses a script to craft LDAP statements based on input from a user, then LDAP injection is potentially a threat. Just as with SQL injection, validation and escaping of input and defensive coding are essential to eliminate this threat.

XML injection is another type of injection attack, where the back-end target is an XML application. Again, input escaping and validation combats this threat. Commands may even attempt to load dynamically linked libraries (DLLs) containing malicious code in a DLL injection attack .

Cross-site scripting is an example of a code injection attack that inserts script code written by an attacker into the web pages created by a developer. We'll discuss cross-site scripting in detail later in this chapter.

### Command Injection Attacks

In some cases, application code may reach back to the operating system to execute a command. This is especially dangerous because an attacker might exploit a flaw in the application and gain the ability to directly manipulate the operating system. For example, consider the simple application shown in Figure 21.4 .

FIGURE 21.4 Account creation page

FIGURE 21.4 Account creation page

This application sets up a new student account for a course. Among other actions, it creates a directory on the server for the student. On a Linux system, the application might use a system() call to send the directory creation command to the underlying operating system. For example, if someone fills in the text box with

`system()`

```

mchapple
```

`mchapple`

the application might use the function call

```

system('mkdir /home/students/mchapple')
```

`system('mkdir /home/students/mchapple')`

to create a home directory for that user. An attacker examining this application might guess that this is how the application works and then supply the input

```

mchapple & rm -rf /home
```

`mchapple & rm -rf /home`

which the application then uses to create the system call:

```

system('mkdir /home/students/mchapple & rm -rf home')
```

`system('mkdir /home/students/mchapple & rm -rf home')`

This sequence of commands deletes the /home directory along with all files and subfolders it contains. The ampersand in this command indicates that the operating system should execute the text after the ampersand as a separate command. This allows the attacker to execute the rm command by exploiting an input field that is only intended to execute a mkdir command.

`/home`

`rm`

`mkdir`
