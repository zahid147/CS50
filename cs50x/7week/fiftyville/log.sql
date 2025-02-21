-- Keep a log of any SQL queries you execute as you solve the mystery.


--query to find the case id and description

SELECT * FROM crime_scene_reports
WHERE year = "2021" AND month = "7" AND day = "28" AND street = "Humphrey Street";

--case_id: 295
--case description: Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
    --Interviews were conducted today with three witnesses who were present at the time
        -- each of their interview transcripts mentions the bakery.


--query to find the suspected licence plate number

SELECT * FROM bakery_security_logs
WHERE year = "2021" AND month = "7" AND day = "28" AND hour >= 9 AND hour <= 10;

--suspects: 5P2BI95, 6P58WS2, 4328GD8, G412CB7, 94KL13X, L93JTIZ, 322W7JE, 0NTHK55


--query to get details of the suspects based on licence plate number

SELECT * FROM people
WHERE license_plate = "5P2BI95"
OR license_plate = "6P58WS2"
OR license_plate = "4328GD8"
OR license_plate = "G412CB7"
OR license_plate = "94KL13X"
OR license_plate = "L93JTIZ"
OR license_plate = "322W7JE"
OR license_plate = "0NTHK55";

--Results:
--name    |  phone_number  | passport_number | license_plate
--Vanessa | (725) 555-4692 | 2963008352      | 5P2BI95
--Barry   | (301) 555-4174 | 7526138472      | 6P58WS2
--Sofia   | (130) 555-0289 | 1695452385      | G412CB7
--Luca    | (389) 555-5198 | 8496433585      | 4328GD8
--Iman    | (829) 555-5269 | 7049073643      | L93JTIZ
--Diana   | (770) 555-1861 | 3592750733      | 322W7JE
--Kelsey  | (499) 555-9472 | 8294398571      | 0NTHK55
--Bruce   | (367) 555-5533 | 5773159633      | 94KL13X

--query to get the interviews related to the theift
SELECT * FROM interviews WHERE month = 7 AND day >= 28;

--Results:

--Ruth: Sometime within ten minutes of the theft,
    --I saw the thief get into a car in the bakery parking lot and drive away.
        --If you have security footage from the bakery parking lot,
            --you might want to look for cars that left the parking lot in that time frame.

--Eugene: I don't know the thief's name, but it was someone I recognized.
    --Earlier this morning, before I arrived at Emma's bakery,
        --I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.

--Raymond: As the thief was leaving the bakery, they called someone who talked to them for less than a minute.
    --In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow.
        --The thief then asked the person on the other end of the phone to purchase the flight ticket.


--query to get the suspected bank account numbers according to Eugene's interview
SELECT * FROM atm_transactions
WHERE day = 28 AND month = 7
AND year = 2021 AND atm_location = "Leggett Street";

--Suspected account numbers: 28500762, 28296815, 76054385, 49610011
    --16153065, 25506511, 81061156, 26013199


--query to get the name of the suspected account holders
SELECT bank_accounts.*,people.name FROM bank_accounts
INNER JOIN people ON bank_accounts.person_id = people.id
WHERE account_number = 28500762
OR account_number = 28296815
OR account_number = 76054385
OR account_number = 49610011
OR account_number = 16153065
OR account_number = 25506511
OR account_number = 81061156
OR account_number = 26013199;

--Filtered results:
--name    |  phone_number  | passport_number | license_plate| person_id
--Luca    | (389) 555-5198 | 8496433585      | 4328GD8      | 28500762
--Iman    | (829) 555-5269 | 7049073643      | L93JTIZ      | 25506511
--Diana   | (770) 555-1861 | 3592750733      | 322W7JE      | 26013199
--Bruce   | (367) 555-5533 | 5773159633      | 94KL13X      | 49610011

--query to get the details of the airport of Fiftyville
SELECT * FROM airports
WHERE city = "Fiftyville";

--Result:
--| id | abbreviation |                full_name                |     city      |
--| 8  | CSF          | Fiftyville Regional Airport             | Fiftyville    |


--query to get the details of earliest flight that left Fiftyville on 29 July
SELECT * FROM flights
WHERE year = 2021 AND month = 7 AND day = 29
AND origin_airport_id = 8
ORDER BY hour;

--Result:
--| id | origin_airport_id | destination_airport_id | year | month | day | hour | minute |
--| 36 | 8                 | 4                      | 2021 | 7     | 29  | 8    | 20     |


--query to get the passport number of the passergers of the selected flight
SELECT * FROM passengers
WHERE flight_id = 36;

--Found the thief!!!
--| flight_id | passport_number | seat | name   | phone_number   | person_id
--| 36        | 5773159633      | 4A   | Bruce  | (367) 555-5533 | 49610011
--Escaped to: LaGuardia Airport, New York City


--query to find Bruce called whom to book the flight according to the interview of Raymond
SELECT * FROM phone_calls
WHERE year = 2021 AND month = 7
AND day = 28 AND caller = "(367) 555-5533";

--Selected result:
--| id  |     caller     |    receiver    | year | month | day | duration*|
--| 233 | (367) 555-5533 | (375) 555-8161 | 2021 | 7     | 28  | 45       |

--query to find the receiver
SELECT * FROM people
WHERE phone_number = "(375) 555-8161";

--Found the accomplice!!!
--|   id   | name  |  phone_number  | passport_number | license_plate |
--| 864400 | Robin | (375) 555-8161 | NULL            | 4V16VO0       |