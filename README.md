# Movie Ticket Booking System

## 1. Introduction
This is a desktop application developed as part of the B.Tech CSE Java Programming case study.
It allows users to manage movies, book tickets, and view ticket history through a simple graphical interface built with Java Swing.
The application runs fully in-memory using Java Collections Framework — no database required.

---

## 2. Objective
To design and implement a Movie Ticket Booking System using Java that demonstrates:
- Object-Oriented Programming (OOP) concepts
- Java Collections Framework (Array, ArrayList, LinkedList, HashMap, TreeMap)
- Java Swing GUI
- Exception Handling and Input Validation

---

## 3. Features

### Movies Tab
- Add a new movie (Name, Genre, Duration, Rating)
- Update an existing movie by Movie ID
- Delete a movie by Movie ID
- Search movie by Movie ID or name
- Sort movies by Name (A–Z)
- Sort movies by Rating (highest first)
- **Add Show for Movie** — add a show time for any movie (click a row to auto-fill Movie ID, then click the orange button)
- Movies displayed in a table: Movie ID | Movie Name | Genre | Duration | Rating

### Book Ticket Tab
- Select movie from dropdown
- Select show time from dropdown
- Enter customer details: Name, Phone (10 digits), Email
- Enter seat number (e.g. A1, B3, C5)
- View available seats in real time — booked seats shown as `[X1]`
- Click **Book Ticket** → confirmation + bill shown instantly
- Click **Refresh Movies** to load newly added movies

### My Tickets Tab
- View all booked tickets in a table: Ticket ID | Customer | Movie | Show Time | Seat | Price
- Search any ticket by Ticket ID
- View full bill for any ticket
- Cancel a ticket (seat becomes available again)

### Billing
- Auto-generated bill shown via popup after booking:
```
--------------------------------
       MOVIE TICKET BILL
--------------------------------
Ticket ID : T001
Customer  : Jaikishan
Movie     : Avengers: Endgame
Show Time : 10:00 AM
Seat      : A3
Price     : Rs.200
--------------------------------
Total     : Rs.200
--------------------------------
```

---

## 4. Technologies Used
- Java 17+
- Java Swing (GUI framework)
- Java Collections Framework
- OOP — Encapsulation, Inheritance, Custom Exception

---

## 5. Java Concepts Used

| Concept              | Where Used                                        |
|----------------------|---------------------------------------------------|
| Class & Object       | Movie, Show, Customer, Ticket, BookingSystem      |
| Encapsulation        | Private fields + Getters/Setters in all models    |
| Constructor          | All model classes                                 |
| Inheritance          | SeatAlreadyBookedException extends Exception      |
| Custom Exception     | SeatAlreadyBookedException.java                   |
| Exception Handling   | bookTicket(), addMovie(), all GUI action methods  |
| toString()           | Overridden in Movie, Show, Customer, Ticket       |
| Static Methods       | Customer.isValidPhone(), Customer.isValidName()   |

---

## 6. Collection Framework Used

| Collection              | Variable                    | Purpose                                          |
|-------------------------|-----------------------------|--------------------------------------------------|
| **Array**               | `String[] seats`            | Fixed 15-seat layout in Show (A1–A5, B1–B5, C1–C5) |
| **ArrayList\<Movie\>**  | `movies`                    | Stores all movies; supports add/delete/search    |
| **ArrayList\<Customer\>** | `customers`               | Stores all registered customers                  |
| **LinkedList\<Ticket\>** | `bookingList`              | Maintains booking history in insertion order     |
| **HashMap\<String, Ticket\>** | `tickets`           | Fast O(1) ticket lookup by Ticket ID             |
| **TreeMap\<String, Show\>** | `shows`               | Stores shows sorted automatically by show time   |

---

## 7. Project Structure

```
MovieTicketBookingSystem/
│
├── src/
│   ├── model/
│   │   ├── Movie.java                    — Movie entity (id, name, genre, duration, rating)
│   │   ├── Show.java                     — Show entity with seat Array, bookSeat(), cancelSeat()
│   │   ├── Customer.java                 — Customer entity with validation
│   │   ├── Ticket.java                   — Ticket entity with getBillInfo()
│   │   └── SeatAlreadyBookedException.java — Custom exception
│   │
│   ├── service/
│   │   └── BookingSystem.java            — All collections + all business logic
│   │
│   ├── gui/
│   │   ├── MainFrame.java                — JFrame with 3-tab layout + header + Exit
│   │   ├── MoviePanel.java               — Movies tab (CRUD + Add Show + Sort)
│   │   ├── BookingPanel.java             — Book Ticket tab (seat selection + booking)
│   │   └── TicketPanel.java              — My Tickets tab (search + cancel + bill)
│   │
│   └── Main.java                         — Entry point, launches MainFrame on EDT
│
├── README.md
└── .gitignore
```

---

## 8. How to Run

### Option A — IntelliJ IDEA (Recommended)
1. Open IntelliJ IDEA → **File → Open** → select the `movietickets` folder
2. Right-click `src` folder → **Mark Directory As** → **Sources Root**
3. Right-click `src/Main.java` → **Run 'Main'**

> If IntelliJ shows import errors: **File → Invalidate Caches → Invalidate and Restart**

### Option B — Terminal / Command Line
```bash
cd /path/to/movietickets/src

# Compile
javac -d . model/SeatAlreadyBookedException.java model/Movie.java model/Customer.java \
         model/Show.java model/Ticket.java service/BookingSystem.java \
         gui/MoviePanel.java gui/BookingPanel.java gui/TicketPanel.java \
         gui/MainFrame.java Main.java

# Run
java Main
```

---

## 9. Sample / Preloaded Data

The application starts with these movies already loaded:

| Movie ID | Movie Name        | Genre    | Duration | Rating |
|----------|-------------------|----------|----------|--------|
| M001     | Avengers: Endgame | Action   | 181 min  | 8.4    |
| M002     | Avatar            | Sci-Fi   | 162 min  | 7.8    |
| M003     | Inception         | Thriller | 148 min  | 8.8    |
| M004     | Interstellar      | Sci-Fi   | 169 min  | 8.6    |

Sample shows are created for the above movies at 10:00 AM, 01:00 PM, 06:00 PM, and 09:00 PM.

**To add a new movie with a show:**
1. Go to **Movies** tab → fill in details → click **Add Movie**
2. Click the new movie's row in the table (auto-fills Movie ID)
3. Click **Add Show for Mo...** (orange button) → enter time e.g. `06:00 PM`
4. Go to **Book Ticket** tab → click **Refresh Movies** → select the movie → show appears

---

## 10. How to Book a Ticket (Step by Step)

1. Go to the **Book Ticket** tab
2. Select a **Movie** from the dropdown
3. Select a **Show** time from the dropdown
4. The right panel shows all available seats (A1–C5)
5. Enter **Customer Name**, **Phone** (10 digits), **Email**
6. Enter a **Seat Number** (e.g. `A3`)
7. Click **Book Ticket**
8. A bill popup appears confirming the booking
9. Go to **My Tickets** tab to see all bookings

---

## 11. Seat Layout

Each show has 15 seats arranged as:
```
A1  A2  A3  A4  A5
B1  B2  B3  B4  B5
C1  C2  C3  C4  C5
```
- Available seats shown normally
- Booked seats shown as `[A1]` in the seat view
- Attempting to rebook a booked seat shows: `SeatAlreadyBookedException`

---

## 12. Validation & Exception Handling

| Scenario                    | Handling                                      |
|-----------------------------|-----------------------------------------------|
| Empty customer name         | Exception with message shown in JOptionPane   |
| Phone not 10 digits         | Regex validation: `phone.matches("\\d{10}")`  |
| Empty movie name            | Exception thrown in addMovie()                |
| Invalid seat number         | Exception: "Invalid seat number"              |
| Seat already booked         | `SeatAlreadyBookedException` thrown + caught  |
| Ticket ID not found         | "Ticket not found" message in JOptionPane     |
| Rating out of range (0–10)  | Validation check in MoviePanel                |

---

## 13. Conclusion

This project demonstrates the use of core Java concepts — OOP, Java Collections Framework, Swing GUI, and Exception Handling — to build a functional, real-world style application.

Different data structures were chosen based on their use case:
- **Array** for fixed-size seat layout
- **ArrayList** for dynamic movie and customer lists
- **LinkedList** for ordered booking history
- **HashMap** for fast ticket lookup by ID
- **TreeMap** for automatically sorted shows by time

The application is simple, clean, and easy to demonstrate in a viva.

---

**Submitted by:** [Your Name]
**Roll No:** [Your Roll Number]
**Subject:** Java Programming
**College:** [Your College Name]
**Year/Semester:** [e.g. 2nd Year / 4th Semester]
