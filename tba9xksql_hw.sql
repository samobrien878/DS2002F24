#World Database Questions#

SELECT name FROM country WHERE continent = "South America";

SELECT Population FROM country WHERE Name = "Germany";

SELECT Name FROM city Where CountryCode = "JPN";

SELECT Name, Population FROM country WHERE Region in ('Western Africa','Eastern Africa')
ORDER BY Population DESC LIMIT 3; 

SELECT Name, LifeExpectancy FROM country WHERE Population BETWEEN 1000000 AND 5000000;

SELECT country.Name FROM country
JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE countrylanguage.Language = 'FRENCH' AND countrylanguage.IsOfficial = 'T';




#Chinook Questions#

SELECT Album.Title FROM Album WHERE ArtistID = 1;

SELECT FirstName, LastName, Email FROM Customer WHERE Country = 'Brazil';

Select Name FROM Playlist;

SELECT COUNT(*) AS TrackCount FROM Track WHERE GenreId = 1;

SELECT FirstName, LastName FROM Employee WHERE ReportsTo = 2; 

SELECT Invoice.CustomerId, SUM(Invoice.Total) as TotalSales 
From Invoice
GROUP BY CustomerId




#Attempt at making the tables in the dataset#

CREATE TABLE `Customer Information` (
    `CustomerID` INT PRIMARY KEY,
    `Name` Text,
    `Email` Text,
    `ZIP` Text);

INSERT INTO `Customer Information` (`CustomerID`, `Name`, `Email`, `ZIP`) VALUES
(1, 'Joe', 'joe@gmail.com', '12345'),(2, 'Fred', 'Fred@gmail.com', '54321'),(3, 'Jan', 'Jan@gmail.com', '12344'),(4, 'Sam', 'Sam@gmail.com', '54322'),(5, 'Bob', 'Bob@gmail.com', '12343');

CREATE TABLE `Employee Info` (
    `EmployeeID` INT PRIMARY KEY,
    `Name` VARCHAR(100),
    `Title` VARCHAR(100),
    `Salary` DECIMAL(10, 2));

INSERT INTO `Employee Info` (`EmployeeID`, `Name`, `Title`, `Salary`) VALUES
(1, 'Levi', 'Cashier', 20000.00),(2, 'Angelica', 'Manager', 50000.00),(3, 'Elizabeth', 'CEO', 100000.00),(4, 'Lawrence', 'Janitor', 30000.00),(5, 'Alexander', 'Sales Agent', 60000.00);

CREATE TABLE `Sales` (
    `CustomerID` INT,
    `UnitsSold` INT,
    `Price_Of_Unit` INT);

INSERT INTO `Sales` (`CustomerID`, `UnitsSold`, `Price_Of_Unit`) VALUES
(1, 5, 600.00),(2, 3, 1000.00),(3, 5, 600.00),(4, 3, 1200.00),(5, 9, 200.00);


#Queries#

SELECT * FROM `Customer Information` WHERE ZIP = 12345;

SELECT 
    ci.Name, 
    ci.CustomerID, 
    s.Price_Of_Unit FROM `Customer Information` ci JOIN `Sales` s  ON ci.CustomerID = s.CustomerID WHERE s.Price_Of_Unit > 500;
    
SELECT Salary, Title FROM `Employee Info` WHERE Salary > 20000
