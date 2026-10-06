\# Movie Ticket Booking System — VIVA Guide

---

## SECTION 1 — CASE STUDY INTRODUCTION

This project is a **Movie Ticket Booking System** built using Java Swing as a desktop application.
It solves the problem of manually managing movie bookings by providing a digital system where a user can add movies, create show times, register customers, book seats, and generate a bill — all in one place.
The application runs completely in-memory using Java Collections, with no external database needed.
It was built as a B.Tech CSE Java Programming case study to demonstrate OOP, Collections, Swing GUI, and Exception Handling in a real-world scenario.

**Main Features:**
- Manage movies (Add, Update, Delete, Search, Sort)
- Add show times for any movie
- Book a seat for a show with customer details
- Auto-generate a bill after booking
- View, search, and cancel tickets

---

### Presentation Introduction (Speak This)

> "Good morning sir/ma'am. My case study is a Movie Ticket Booking System developed using Java Swing.
> The purpose of this project is to digitally manage movie bookings — a user can add movies, create shows, select a seat, and book a ticket with auto-generated billing.
> I have used Java Collections like ArrayList, LinkedList, HashMap, and TreeMap to store and manage data, and Java Swing for the graphical interface.
> The project demonstrates Object-Oriented Programming, the Collections Framework, Exception Handling, and basic CRUD operations.
> I will now explain the project in detail."

---

## SECTION 2 — WHAT I HAVE MADE

A Java Swing desktop application with 3 main screens (tabs):

| Module | What it does |
|--------|-------------|
| Movie Management | Add, update, delete, search, and sort movies; also add show times |
| Show Management | Create show times for movies; shows stored sorted by time |
| Seat Booking | Select movie + show, pick a seat from A1–C5 layout, book ticket |
| Customer Management | Customer is auto-registered when a ticket is booked |
| Ticket Management | View all tickets, search by Ticket ID, cancel a ticket |
| Billing | Auto-generate a formatted bill shown via popup after booking |

---

## SECTION 3 — PROJECT FLOW

```
Main.java
    ↓  Launches the app on Swing's Event Dispatch Thread
MainFrame.java
    ↓  Creates the JFrame with 3 tabs
MoviePanel  →  Add movies and show times
    ↓
BookingPanel  →  Select movie + show + seat + enter customer details
    ↓
BookingSystem.bookTicket()  →  Validates, books seat, creates Ticket object
    ↓
Ticket.getBillInfo()  →  Formats the bill string
    ↓
JOptionPane  →  Displays bill to user
    ↓
TicketPanel  →  View, search, or cancel tickets
```

Each step in one line:
- `Main.java` — starts the app safely on the Swing thread
- `MainFrame.java` — builds the window with tabs
- `MoviePanel` — handles all movie and show operations
- `BookingPanel` — handles customer input and seat selection
- `BookingSystem` — contains all collections and all logic
- `Ticket` — holds booking details and generates bill text
- `TicketPanel` — lets user search and cancel bookings

---

## SECTION 4 — JAVA FILE EXPLANATION

### Main.java
**Purpose:** Entry point of the application.
**Important code:** `SwingUtilities.invokeLater(() -> new MainFrame())` — runs GUI on the Event Dispatch Thread.
**Viva line:** "Main.java launches the application safely on Swing's Event Dispatch Thread."

---

### model/Movie.java
**Purpose:** Represents a movie with its details.
**Important variables:** `movieId`, `movieName`, `genre`, `duration`, `rating`
**Important methods:** Constructor, getters, setters, `toString()`
**Viva line:** "Movie.java is a model class that stores one movie's data using encapsulation — private fields with public getters and setters."

---

### model/Show.java
**Purpose:** Represents a cinema show with a seat layout.
**Important variables:** `String[] seats` (15 seats), `boolean[] seatBooked`, `showId`, `movie`, `showTime`
**Important methods:** `bookSeat()`, `cancelSeat()`, `isSeatAvailable()`, `getAllSeatsInfo()`
**Viva line:** "Show.java uses a String Array to store 15 fixed seats (A1–C5) and a boolean Array to track which seats are booked."

---

### model/Customer.java
**Purpose:** Stores customer information registered during booking.
**Important variables:** `customerId`, `name`, `phone`, `email`
**Important methods:** `isValidPhone()` (static), `isValidName()` (static), getters, setters
**Viva line:** "Customer.java has static validation methods — isValidPhone() uses regex `\\d{10}` to check 10-digit phone numbers."

---

### model/Ticket.java
**Purpose:** Represents a booked ticket and generates the bill.
**Important variables:** `ticketId`, `customer`, `movie`, `show`, `seatNumber`, `price`
**Important methods:** `getBillInfo()` — returns formatted bill string
**Viva line:** "Ticket.java holds all booking details and its getBillInfo() method returns a formatted bill shown to the user."

---

### model/SeatAlreadyBookedException.java
**Purpose:** Custom exception thrown when a user tries to book an already-booked seat.
**Important code:** `extends Exception` — inherits from Java's Exception class
**Viva line:** "SeatAlreadyBookedException is a custom checked exception that I created to handle the specific case of a duplicate seat booking."

---

### service/BookingSystem.java
**Purpose:** The brain of the application — holds all 5 collections and all business logic.
**Important variables:** `ArrayList<Movie> movies`, `ArrayList<Customer> customers`, `LinkedList<Ticket> bookingList`, `HashMap<String, Ticket> tickets`, `TreeMap<String, Show> shows`
**Important methods:** `addMovie()`, `updateMovie()`, `deleteMovie()`, `searchMovie()`, `searchMovieByName()`, `addCustomer()`, `addShow()`, `bookTicket()`, `cancelTicket()`, `searchTicket()`, `getMoviesSortedByName()`, `getMoviesSortedByRating()`
**Viva line:** "BookingSystem.java is the service class that contains all five collections and all the application logic in one place."

---

### gui/MainFrame.java
**Purpose:** The main JFrame window with header, 3 tabs (Movies / Book Ticket / My Tickets), and Exit button.
**Important code:** `JTabbedPane` with `ChangeListener` — refreshes the relevant panel when user switches tabs.
**Viva line:** "MainFrame.java creates the main window using JFrame and JTabbedPane, and refreshes each panel when the user switches tabs."

---

### gui/MoviePanel.java
**Purpose:** Movies tab — CRUD for movies + Add Show button.
**Important code:** `JTable` with `DefaultTableModel`, row click auto-fills Movie ID field, 8 action buttons.
**Viva line:** "MoviePanel.java handles all movie operations including adding show times; clicking a table row auto-fills the Movie ID for quick update/delete."

---

### gui/BookingPanel.java
**Purpose:** Book Ticket tab — movie/show selection, customer form, seat view, book button.
**Important code:** `JComboBox` for movie and show selection; `cmbMovie.addActionListener` updates shows when movie changes; calls `bookingSystem.bookTicket()`.
**Viva line:** "BookingPanel.java uses two JComboBox dropdowns where selecting a movie automatically loads its available shows."

---

### gui/TicketPanel.java
**Purpose:** My Tickets tab — view all tickets, search by ID, view bill, cancel ticket.
**Important code:** Iterates over `LinkedList<Ticket> bookingList` to populate JTable; uses `tickets.get(ticketId)` for search.
**Viva line:** "TicketPanel.java displays tickets from the LinkedList in booking order and uses HashMap.get() for fast ticket search."

---

## SECTION 5 — JAVA CONCEPTS USED

| Concept | One-line meaning | Where used in my project | Example |
|---------|-----------------|--------------------------|---------|
| Class | Blueprint for creating objects | Movie, Show, Customer, Ticket, BookingSystem | `public class Movie { }` |
| Object | Instance of a class | `new Movie(id, name, ...)` in BookingSystem | `Movie movie = new Movie(...)` |
| Constructor | Initializes object when created | All model classes | `public Movie(String id, ...)` |
| Encapsulation | Private fields + public getters/setters | Movie, Customer, Show, Ticket | `private String movieName;` + `getMovieName()` |
| Inheritance | Child class extends parent | SeatAlreadyBookedException extends Exception | `extends Exception` |
| Polymorphism | `toString()` overridden | All model classes override Object's toString() | `@Override public String toString()` |
| Abstraction | Hiding internal logic behind methods | BookingSystem hides all logic from GUI panels | GUI calls `bookTicket()`, not the internals |
| Static Methods | Methods called without creating object | Customer.isValidPhone(), Customer.isValidName() | `Customer.isValidPhone("9876543210")` |
| Array | Fixed-size collection | `String[] seats` in Show.java — 15 seats | `seats = new String[15]` |
| ArrayList | Dynamic resizable list | `ArrayList<Movie> movies` in BookingSystem | `movies.add(movie)` |
| LinkedList | Ordered list, preserves insertion order | `LinkedList<Ticket> bookingList` | `bookingList.add(ticket)` |
| HashMap | Key-value pair, O(1) lookup | `HashMap<String, Ticket> tickets` | `tickets.get("T001")` |
| TreeMap | Sorted map, auto-sorts by key | `TreeMap<String, Show> shows` | Keys are showTime+showId, auto-sorted |
| CRUD | Create, Read, Update, Delete | Full CRUD on movies; Create+Read for tickets | `addMovie()`, `updateMovie()`, `deleteMovie()` |
| Searching | Finding specific object | `searchMovie()`, `searchTicket()`, `searchMovieByName()` | Loop through ArrayList or HashMap.get() |
| Sorting | Ordering a list | `getMoviesSortedByName()`, `getMoviesSortedByRating()` | `Collections.sort()` with `Comparator` |
| Exception Handling | try-catch to handle runtime errors | `bookTicket()` throws & catches exceptions | `throw new SeatAlreadyBookedException(...)` |
| Validation | Checking input before processing | Phone: `phone.matches("\\d{10}")`, name not empty | `Customer.isValidPhone(phone)` |
| Event Handling | Button click triggers action | All JButton clicks use `ActionListener` | `btnAdd.addActionListener(e -> addMovie())` |

---

## SECTION 6 — OOP CONCEPTS

| OOP Concept | One-line Meaning | My Project Example |
|-------------|-----------------|-------------------|
| Class | Template/blueprint for objects | `Movie`, `Show`, `Customer`, `Ticket` are all classes |
| Object | Actual instance created from class | `new Movie("M001", "Avatar", ...)` is a Movie object |
| Encapsulation | Fields private, accessed via methods only | `private String movieName` with `getMovieName()` / `setMovieName()` |
| Inheritance | One class gets features of another | `SeatAlreadyBookedException extends Exception` |
| Polymorphism | Same method, different behavior | `toString()` overridden in Movie, Show, Customer, Ticket |
| Abstraction | User sees only what they need | GUI calls `bookingSystem.bookTicket()` without knowing internal logic |
| Constructor | Special method to initialize object | `public Movie(String movieId, String movieName, ...)` |

---

## SECTION 7 — COLLECTIONS USED

| Collection | Variable name in my code | Purpose | Simple Example |
|-----------|--------------------------|---------|----------------|
| Array | `String[] seats`, `boolean[] seatBooked` | Fixed 15-seat layout in Show (A1–C5) | `seats = new String[15]` |
| ArrayList | `ArrayList<Movie> movies` | Stores all movies; supports dynamic add/remove | `movies.add(movie)` |
| ArrayList | `ArrayList<Customer> customers` | Stores all customers registered during booking | `customers.add(customer)` |
| LinkedList | `LinkedList<Ticket> bookingList` | Maintains booking history in order of booking | `bookingList.add(ticket)` |
| HashMap | `HashMap<String, Ticket> tickets` | Stores tickets; Ticket ID is key for fast lookup | `tickets.get("T001")` |
| TreeMap | `TreeMap<String, Show> shows` | Stores shows; keys are time-based so shows auto-sort | `shows.put(showTime + "_" + showId, show)` |

---

## SECTION 8 — BASIC JAVA QUICK REVISION

| Topic | One-line meaning |
|-------|-----------------|
| Variable | Named storage for a value — `String movieName` |
| Data Type | Type of value — `int`, `double`, `String`, `boolean` |
| if/else | Conditional — execute code based on condition |
| Loop | Repeat code — `for`, `while` used to iterate through seats, movies |
| Method | Reusable block of code — `addMovie()`, `bookSeat()` |
| Constructor | Special method that runs when object is created |
| Array | Fixed-size, same-type collection — `String[] seats` |
| Collection | Dynamic data structures — ArrayList, LinkedList, HashMap, TreeMap |
| Class | Blueprint — `Movie`, `Customer` are classes |
| Object | Instance of a class — `new Movie(...)` creates a Movie object |
| Exception | Runtime error handled by try-catch — `SeatAlreadyBookedException` |

---

## SECTION 9 — SWING / UI COMPONENTS

| UI Component | What it does | Where I used it |
|-------------|-------------|----------------|
| `JFrame` | Main application window | `MainFrame extends JFrame` — the whole app window |
| `JPanel` | Container for grouping components | Used in every panel: form panel, button panel, seat panel |
| `JLabel` | Display-only text | Field labels like "Movie Name:", "Phone:", "Select Show:" |
| `JTextField` | Single-line text input | `txtMovieName`, `txtPhone`, `txtSeat`, `txtTicketId` |
| `JTextArea` | Multi-line text display | `txtAvailableSeats` in BookingPanel — shows seat layout |
| `JButton` | Clickable button | Add Movie, Book Ticket, Cancel Ticket, Exit, etc. |
| `JComboBox` | Dropdown selection | `cmbMovie`, `cmbShow` in BookingPanel |
| `JTable` | Tabular data display | Movie table, Ticket table — backed by `DefaultTableModel` |
| `JTabbedPane` | Tab-based navigation | 3 tabs: Movies / Book Ticket / My Tickets in MainFrame |
| `JScrollPane` | Scrollable wrapper | Wraps JTable and JTextArea so they scroll |
| `JOptionPane` | Popup dialogs | Bill popup, error messages, confirm dialogs |

**Layouts used:**
| Layout | Where |
|--------|-------|
| `BorderLayout` | MainFrame, MoviePanel, BookingPanel, TicketPanel |
| `GridLayout` | Form panels inside MoviePanel and BookingPanel |
| `FlowLayout` | Button panels and footer |

**Event Handling:**
- `ActionListener` — attached to every JButton via `addActionListener(e -> method())`
- `ChangeListener` — on `JTabbedPane` in MainFrame to refresh panels on tab switch
- `ListSelectionListener` — on movie table in MoviePanel to auto-fill Movie ID on row click

---

## SECTION 10 — PROJECT FEATURES

| Feature | What actually happens |
|---------|----------------------|
| Add Movie | Creates Movie object, adds to `ArrayList<Movie> movies` with auto-generated ID (M001, M002...) |
| Update Movie | Searches `movies` ArrayList by ID, calls setters to update fields |
| Delete Movie | Finds movie in ArrayList, removes it; shows confirmation dialog |
| Search Movie | Searches by ID (exact match) or by name (contains match) using for loop |
| Sort by Name | `Collections.sort()` with `Comparator.comparing(Movie::getMovieName)` |
| Sort by Rating | `list.sort()` with lambda — highest rating first |
| Add Show | Creates Show object with 15 seats, puts in TreeMap with time as key |
| Book Ticket | Validates input → books seat in Show → creates Ticket → stores in HashMap + LinkedList |
| View Available Seats | Calls `show.getAllSeatsInfo()` — available shown normally, booked shown as `[A1]` |
| Cancel Ticket | Removes from HashMap + LinkedList, calls `cancelSeat()` to free the seat |
| Search Ticket | `tickets.get(ticketId)` — direct HashMap lookup |
| View Bill | Calls `ticket.getBillInfo()` and shows in JOptionPane |

---

## SECTION 11 — EXCEPTION HANDLING & VALIDATION

| Situation | How my project handles it |
|-----------|--------------------------|
| Seat already booked | `SeatAlreadyBookedException` thrown in `bookTicket()`, caught in BookingPanel, shows warning popup |
| Empty customer name | `Customer.isValidName()` returns false → `throw new Exception("Customer name cannot be empty.")` |
| Invalid phone | `Customer.isValidPhone()` uses `phone.matches("\\d{10}")` → throws exception if fails |
| Invalid seat number | Loop checks all 15 seats in `String[] seats` → throws `"Invalid seat number"` if not found |
| Ticket ID not found | `tickets.get(ticketId)` returns null → shows "Ticket not found" in JOptionPane |
| Empty movie name | Checked in `MoviePanel.addMovie()` → `throw new Exception("Movie name cannot be empty.")` |
| Rating out of range | Checked in MoviePanel → `if (rating < 0 || rating > 10) throw new Exception(...)` |

---

## SECTION 12 — CRUD / SEARCH / SORTING

| Concept | Meaning | Used for in my project |
|---------|---------|----------------------|
| Create | Add new data | `addMovie()`, `addCustomer()`, `addShow()`, `bookTicket()` |
| Read | Display/fetch data | `getMovies()`, `getBookingList()`, `searchTicket()` |
| Update | Modify existing data | `updateMovie()` — updates name, genre, duration, rating |
| Delete | Remove data | `deleteMovie()`, `cancelTicket()` |
| Search | Find specific data | `searchMovie()` by ID, `searchMovieByName()` by name, `searchTicket()` via HashMap |
| Sort | Order data | `getMoviesSortedByName()` via `Collections.sort()`, `getMoviesSortedByRating()` via lambda |

---

## SECTION 13 — HOW TO EXPLAIN MY CODE

**1. Main.java**
"Main.java is the entry point. It uses `SwingUtilities.invokeLater()` to launch the GUI safely on the Event Dispatch Thread, which is the correct way to start a Swing application."

**2. Model classes**
"I have four model classes — Movie, Show, Customer, and Ticket. Each class has private fields, a constructor, and getters/setters. Show also manages the seat Array. Ticket has a getBillInfo() method."

**3. BookingSystem.java**
"BookingSystem is the service class. It holds all five collections and all the logic. GUI panels never manage data directly — they always call BookingSystem methods."

**4. GUI files**
"MainFrame creates the window. MoviePanel handles movies. BookingPanel handles ticket booking. TicketPanel shows all bookings. Each panel gets a reference to the same BookingSystem object."

**5. Booking process**
"When the user clicks Book Ticket, BookingPanel calls `bookingSystem.bookTicket()`. That method validates the input, checks seat availability, registers the customer, creates a Ticket object, stores it in HashMap and LinkedList, and returns the ticket."

**6. Ticket generation**
"After booking, BookingPanel calls `ticket.getBillInfo()` which returns a formatted bill string. This is shown using `JOptionPane.showMessageDialog()` as a popup."

---

## SECTION 14 — COMPLETE PRESENTATION SCRIPT

> "Good morning sir/ma'am.
>
> My case study is a **Movie Ticket Booking System**, a Java Swing desktop application.
>
> **What I made:** I created a fully working GUI application where a user can add movies, create show times, book seats, and generate bills — all from one screen.
>
> **Why I made it:** To demonstrate the use of Java Collections Framework, OOP concepts, Swing GUI, and Exception Handling in a real-world project.
>
> **Main features:** Movie CRUD with sorting and search, show management, seat booking with visual seat layout, automatic bill generation, and ticket cancellation.
>
> **Project flow:** The application starts from Main.java, which launches MainFrame. MainFrame has three tabs — Movies, Book Ticket, and My Tickets. All data is managed by BookingSystem.java.
>
> **Java concepts I used:**
> - OOP: encapsulation in all model classes, inheritance in my custom exception, polymorphism via toString() override.
> - Collections: Array for fixed seats, ArrayList for movies and customers, LinkedList for booking order, HashMap for fast ticket lookup, TreeMap for sorted shows.
> - Exception Handling: I created a custom exception called SeatAlreadyBookedException which is thrown when a seat is already booked.
> - Sorting: Movies can be sorted by name using Collections.sort() and by rating using a lambda Comparator.
>
> **GUI:** I used JFrame, JTabbedPane, JTable, JComboBox, JTextField, JButton, and JOptionPane.
>
> **Important files:** BookingSystem.java is the core — it has all five collections declared as fields and all methods for CRUD, search, sort, booking, and cancellation.
>
> **Booking process:** User selects movie and show, enters customer details, picks a seat. System validates input, books the seat in the Show's Array, creates a Ticket, stores it in HashMap and LinkedList, and shows a bill popup.
>
> **Conclusion:** This project helped me practically apply Java Collections, OOP, Swing, and Exception Handling. Thank you."

---

## SECTION 15 — VIVA QUESTIONS & ANSWERS

### Basic Java — 15 Questions

**Q1. What is a variable?**
A: A named memory location that stores a value. Example: `String movieName = "Avatar";`

**Q2. What is a data type?**
A: Specifies what kind of value a variable holds. I used `String`, `int`, `double`, `boolean`.

**Q3. What is a method?**
A: A reusable block of code. Example: `addMovie()`, `bookSeat()` in my project.

**Q4. What is a constructor?**
A: A special method that runs when an object is created to set initial values. All my model classes have constructors.

**Q5. What is static in Java?**
A: Static means the method/variable belongs to the class, not an object. I used `Customer.isValidPhone()` and `Customer.isValidName()` as static methods.

**Q6. What is `this` keyword?**
A: Refers to the current object. I used `this.movieName = movieName` in constructors to distinguish field from parameter.

**Q7. What is `@Override`?**
A: Annotation that tells Java a method is overriding a parent class method. I used it for `toString()` in all model classes.

**Q8. What is `toString()`?**
A: A method from the Object class that returns a String representation. I overrode it in Movie, Show, Customer, Ticket.

**Q9. What is a for-each loop?**
A: `for (Movie m : movies)` — loops through every element in a collection. Used throughout BookingSystem.

**Q10. What is `null` in Java?**
A: Represents absence of a value. My search methods return `null` when not found — e.g., `searchMovie()` returns null if not found.

**Q11. What is `try-catch`?**
A: Used to handle exceptions. `try` block contains risky code, `catch` handles the error gracefully.

**Q12. What is `throw`?**
A: Used to manually raise an exception. Example: `throw new SeatAlreadyBookedException("Seat A3 is already booked!");`

**Q13. What is `throws` in method signature?**
A: Declares that a method may throw an exception. `bookTicket()` has `throws SeatAlreadyBookedException, Exception`.

**Q14. What is `SwingUtilities.invokeLater()`?**
A: Ensures the Swing GUI is created on the Event Dispatch Thread, which is the safe way to start a Swing app.

**Q15. What is `String.format()`?**
A: Formats a string with placeholders. I used `String.format("%03d", movieCounter++)` to generate IDs like M001, M002.

---

### OOP — 15 Questions

**Q1. What are the four pillars of OOP?**
A: Encapsulation, Inheritance, Polymorphism, Abstraction.

**Q2. How did you use encapsulation?**
A: All fields in Movie, Customer, Ticket, Show are `private`. I access them only through public getters and setters.

**Q3. How did you use inheritance?**
A: `SeatAlreadyBookedException extends Exception` — it inherits all properties of Exception and adds a custom message.

**Q4. How did you use polymorphism?**
A: I overrode `toString()` in Movie, Show, Customer, and Ticket — same method name, different output for each class.

**Q5. How did you use abstraction?**
A: GUI panels only call `bookingSystem.bookTicket()` — they don't know how it works internally. The implementation is hidden.

**Q6. What is a class vs an object?**
A: Class is a blueprint (Movie.java). Object is an instance — `new Movie("M001", "Avatar", ...)` creates a Movie object.

**Q7. Can you show a constructor from your project?**
A: `public Movie(String movieId, String movieName, String genre, int duration, double rating)` — takes 5 parameters and initializes all fields.

**Q8. What is the difference between a getter and setter?**
A: Getter returns the value (`getMovieName()`). Setter changes the value (`setMovieName("Avatar")`).

**Q9. Why did you make fields private?**
A: To protect data — no class can directly change `movieName` without going through `setMovieName()`. This is encapsulation.

**Q10. What does `extends Exception` mean?**
A: My `SeatAlreadyBookedException` class inherits from Java's Exception class — so it can be thrown and caught like any standard exception.

**Q11. How many classes does your project have?**
A: 11 Java files total — Movie, Show, Customer, Ticket, SeatAlreadyBookedException (model), BookingSystem (service), MainFrame, MoviePanel, BookingPanel, TicketPanel (GUI), and Main.

**Q12. What is a model class?**
A: A class that only holds data and has no business logic — Movie, Customer, Show, Ticket are model classes.

**Q13. What is a service class?**
A: A class that contains business logic. BookingSystem.java is my service class.

**Q14. Is there a real-world relation between your classes?**
A: Yes — a Ticket HAS-A Customer, HAS-A Movie, and HAS-A Show. A Show HAS-A Movie. This is called composition (HAS-A relationship).

**Q15. Where did you use method overriding?**
A: `toString()` is overridden in all four model classes. Example: Movie's toString() returns `"M001 | Avatar | Sci-Fi | 162 min | Rating: 7.8"`.

---

### Collections — 10 Questions

**Q1. What is the Collections Framework?**
A: A set of Java classes and interfaces for storing and managing groups of objects — ArrayList, LinkedList, HashMap, TreeMap, etc.

**Q2. Where did you use Array?**
A: In Show.java — `String[] seats = new String[15]` stores the 15 seat names (A1–C5). Size is fixed because a cinema hall doesn't change.

**Q3. Where did you use ArrayList?**
A: `ArrayList<Movie> movies` stores all movies. `ArrayList<Customer> customers` stores all customers. ArrayList grows dynamically when I add items.

**Q4. Why ArrayList and not Array for movies?**
A: Because movies can be added or deleted at runtime. Array has fixed size; ArrayList resizes automatically.

**Q5. Where did you use LinkedList?**
A: `LinkedList<Ticket> bookingList` stores all booked tickets in booking order. First booked appears first in the My Tickets tab.

**Q6. Where did you use HashMap?**
A: `HashMap<String, Ticket> tickets` stores tickets with Ticket ID as key. `tickets.get("T001")` finds the ticket instantly — O(1) lookup.

**Q7. Why HashMap for tickets and not ArrayList?**
A: HashMap gives O(1) lookup by Ticket ID — much faster than looping through an ArrayList for every search.

**Q8. Where did you use TreeMap?**
A: `TreeMap<String, Show> shows` stores all shows. Key is `showTime + "_" + showId`. TreeMap auto-sorts keys alphabetically, so shows appear in time order.

**Q9. How did you sort movies?**
A: `Collections.sort(sorted, Comparator.comparing(Movie::getMovieName))` for name sort. `sorted.sort((m1, m2) -> Double.compare(m2.getRating(), m1.getRating()))` for rating sort.

**Q10. Can you tell all 5 collections and one reason for each?**
A: Array — fixed seats; ArrayList — dynamic movie list; LinkedList — ordered booking history; HashMap — fast ticket search; TreeMap — auto-sorted shows.

---

### Swing/GUI — 10 Questions

**Q1. What is JFrame?**
A: The main application window. `MainFrame extends JFrame` is my main window.

**Q2. What is JPanel?**
A: A container that groups components. I used separate JPanels for form fields, buttons, and the seat display area.

**Q3. What is JTable?**
A: Displays data in rows and columns. I used it in MoviePanel (movie list) and TicketPanel (ticket list) with DefaultTableModel.

**Q4. What is JComboBox?**
A: A dropdown selection component. `cmbMovie` and `cmbShow` in BookingPanel let the user select a movie and show time.

**Q5. What is JOptionPane?**
A: A ready-made popup dialog. I used it for the bill popup, error messages, and confirm-before-delete dialogs.

**Q6. What is ActionListener?**
A: An interface for handling button clicks. Every JButton uses `addActionListener(e -> method())` to call a method when clicked.

**Q7. What is JTabbedPane?**
A: A component that provides tab-based navigation. My MainFrame has 3 tabs — Movies, Book Ticket, My Tickets.

**Q8. What is BorderLayout?**
A: A layout that divides the container into 5 regions: NORTH, SOUTH, EAST, WEST, CENTER. Used in MainFrame and all panels.

**Q9. What is the Event Dispatch Thread?**
A: A special Swing thread that handles all GUI events. `SwingUtilities.invokeLater()` in Main.java ensures the GUI starts on this thread.

**Q10. What is DefaultTableModel?**
A: A flexible table model for JTable. I used it in MoviePanel and TicketPanel to add/remove rows dynamically: `tableModel.addRow(...)` and `tableModel.setRowCount(0)`.

---

### Project-Specific — 15 Questions

**Q1. What happens when I click "Book Ticket"?**
A: BookingPanel calls `bookingSystem.bookTicket()` with customer details, show ID, and seat. It validates input, checks seat, creates a Customer and Ticket object, stores ticket in HashMap and LinkedList, and returns the ticket for bill display.

**Q2. How do you prevent double-booking of a seat?**
A: `Show.isSeatAvailable()` checks `seatBooked[i]` for the seat. If already true, `SeatAlreadyBookedException` is thrown and the booking is rejected.

**Q3. How is the Ticket ID generated?**
A: `"T" + String.format("%03d", ticketCounter++)` — produces T001, T002, T003 automatically.

**Q4. How is the Movie ID generated?**
A: `"M" + String.format("%03d", movieCounter++)` — produces M001, M002, M003 automatically.

**Q5. What happens when a ticket is cancelled?**
A: `cancelTicket()` looks up the ticket in HashMap, calls `show.cancelSeat()` to set `seatBooked[i] = false`, then removes the ticket from both HashMap and LinkedList.

**Q6. How are shows sorted?**
A: TreeMap sorts automatically by key. The key is `showTime + "_" + showId` (e.g., `"01:00 PM_S002"`), so shows appear in time order.

**Q7. Where is sample data loaded?**
A: In `BookingSystem.loadSampleData()` called from the constructor — 4 movies (Avengers, Avatar, Inception, Interstellar) and 4 shows are added on startup.

**Q8. How does the seat view work?**
A: `bookingSystem.getAvailableSeats(showId)` calls `show.getAllSeatsInfo()` which loops through `seats[]` — available seats shown normally, booked as `[A1]`.

**Q9. How do you add a show for a new movie?**
A: In the Movies tab, click the movie row (auto-fills Movie ID), then click "Add Show for Movie" (orange button) and enter a time like `06:00 PM`.

**Q10. How is the bill generated?**
A: `Ticket.getBillInfo()` returns a formatted String with ticket ID, customer, movie, show time, seat, price, and total. Shown in `JOptionPane.showMessageDialog()`.

**Q11. Where is customer data stored?**
A: In `ArrayList<Customer> customers` in BookingSystem. Customer is auto-created when a ticket is booked — the user doesn't register separately.

**Q12. What validation exists in your project?**
A: Name not empty (`isValidName()`), phone must be exactly 10 digits (`isValidPhone()` using regex), rating between 0–10, seat must exist, seat must be available, Ticket ID must exist before cancel/search.

**Q13. How does search by movie name work?**
A: `searchMovieByName()` loops through `ArrayList<Movie> movies` and checks if `m.getMovieName().toLowerCase().contains(name.toLowerCase())` — it's a partial match search.

**Q14. Why did you use LinkedList for bookingList instead of ArrayList?**
A: LinkedList preserves insertion order (good for a booking queue) and is efficient for add/remove from both ends. It makes the booking history display in the order tickets were booked.

**Q15. How many seats are in each show?**
A: 15 seats — 3 rows (A, B, C) × 5 columns (1–5), giving A1 to C5. Stored in `String[] seats = new String[15]` in Show.java.

---

## SECTION 16 — QUICK REVISION CHEAT SHEET

---

### Project
| | |
|-|-|
| Name | Movie Ticket Booking System |
| Purpose | Book cinema tickets digitally with billing |
| Tech | Java 17 + Swing + Collections |
| Data storage | In-memory (no database) |

---

### Files
| File | Role |
|------|------|
| `Main.java` | Entry point — launches MainFrame on EDT |
| `Movie.java` | Model — movie data + getters/setters |
| `Show.java` | Model — seats Array + bookSeat/cancelSeat |
| `Customer.java` | Model — customer data + static validation |
| `Ticket.java` | Model — booking details + getBillInfo() |
| `SeatAlreadyBookedException.java` | Custom exception — extends Exception |
| `BookingSystem.java` | Service — all 5 collections + all logic |
| `MainFrame.java` | GUI — JFrame + JTabbedPane + 3 panels |
| `MoviePanel.java` | GUI — movie CRUD + Add Show button |
| `BookingPanel.java` | GUI — booking form + seat view |
| `TicketPanel.java` | GUI — ticket list + search + cancel |

---

### OOP
| Concept | My Example |
|---------|-----------|
| Class | `Movie`, `Show`, `Customer`, `Ticket` |
| Object | `new Movie("M001", "Avatar", ...)` |
| Encapsulation | `private String movieName` + `getMovieName()` |
| Inheritance | `SeatAlreadyBookedException extends Exception` |
| Polymorphism | `toString()` overridden in all model classes |
| Abstraction | GUI calls `bookTicket()`, doesn't know internals |
| Constructor | `public Movie(String id, String name, ...)` |

---

### Collections
| Collection | Variable | Why this one? |
|-----------|----------|--------------|
| Array | `String[] seats` | Fixed 15 seats — size never changes |
| ArrayList | `ArrayList<Movie> movies` | Dynamic — movies added/removed |
| ArrayList | `ArrayList<Customer> customers` | Dynamic — customers grow with bookings |
| LinkedList | `LinkedList<Ticket> bookingList` | Ordered — booking history in sequence |
| HashMap | `HashMap<String, Ticket> tickets` | Fast lookup — `tickets.get("T001")` |
| TreeMap | `TreeMap<String, Show> shows` | Auto-sorted — shows by time |

---

### GUI Components
| Component | Used for |
|-----------|---------|
| `JFrame` | Main window (`MainFrame extends JFrame`) |
| `JTabbedPane` | 3 tabs: Movies / Book Ticket / My Tickets |
| `JPanel` | Group form fields, buttons, seat area |
| `JLabel` | Field labels ("Movie Name:", "Phone:") |
| `JTextField` | Text input fields |
| `JTextArea` | Seat layout display in BookingPanel |
| `JButton` | All action buttons |
| `JComboBox` | Movie and Show dropdowns in BookingPanel |
| `JTable` | Movie list, Ticket list |
| `JScrollPane` | Makes JTable and JTextArea scrollable |
| `JOptionPane` | Bill popup, errors, confirm dialogs |

---

### Java Essentials
| Topic | Short Answer |
|-------|-------------|
| Variable | Named storage — `String movieName` |
| Data Type | `int`, `double`, `String`, `boolean` |
| if/else | Conditional logic — used in all validations |
| Loop | `for (Movie m : movies)` — iterate collections |
| Method | Reusable code — `addMovie()`, `bookSeat()` |
| Static | Class-level — `Customer.isValidPhone()` |
| try-catch | Handle exceptions — used in `bookTicket()` |
| throw | Manually raise error — `throw new SeatAlreadyBookedException(...)` |
| Regex | `phone.matches("\\d{10}")` — validates 10-digit phone |

---

### Project Flow
```
Main.java → MainFrame → [3 Tabs]
    Movies Tab: addMovie() / updateMovie() / deleteMovie() / addShow()
    Book Ticket Tab: bookTicket() → SeatBooked → Ticket created → Bill shown
    My Tickets Tab: searchTicket() / cancelTicket() / getBillInfo()
```

---

### Most Important Viva Lines (Memorize These)

1. "BookingSystem.java has all 5 collections and all the logic."
2. "Array is used in Show.java for 15 fixed seats — `String[] seats = new String[15]`."
3. "ArrayList stores movies and customers because size changes dynamically."
4. "LinkedList stores bookingList to preserve the order of bookings."
5. "HashMap stores tickets — `tickets.get("T001")` gives O(1) lookup."
6. "TreeMap stores shows — auto-sorted by show time as the key."
7. "SeatAlreadyBookedException extends Exception — it's my custom exception."
8. "Encapsulation: all fields are private, accessed via getters and setters."
9. "Polymorphism: toString() is overridden in Movie, Show, Customer, Ticket."
10. "getBillInfo() in Ticket.java formats and returns the complete bill string."
11. "Customer is auto-registered when a ticket is booked — no separate registration."
12. "SwingUtilities.invokeLater() starts the GUI safely on the Event Dispatch Thread."
13. "`Collections.sort()` with `Comparator` is used to sort movies by name or rating."
14. "Validation: phone uses `phone.matches(\"\\d{10}\")`, name uses `!name.trim().isEmpty()`."
15. "On cancel: seat is freed in Show's Array, ticket removed from HashMap and LinkedList."
