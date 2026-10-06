# CODE.md — Movie Ticket Booking System
## Line-by-Line Code Explanation (Simple Words)

---

# FILE 1 — Main.java
### Role: Starting point of the entire application

```java
import gui.MainFrame;
```
> We are telling Java: "I need the MainFrame class from the gui folder."

```java
import javax.swing.SwingUtilities;
```
> SwingUtilities is a helper class from Java Swing. We need it to safely start the GUI.

```java
public class Main {
```
> We created a class named Main. Every Java program needs at least one class.

```java
    public static void main(String[] args) {
```
> This is the main method — Java always starts running from here.
> `public` = anyone can access it.
> `static` = you don't need to create an object to use it.
> `void` = it returns nothing.
> `String[] args` = accepts command line arguments (we don't use them here).

```java
        SwingUtilities.invokeLater(() -> {
            new MainFrame();
        });
```
> `SwingUtilities.invokeLater()` says: "Run this code on the Event Dispatch Thread."
> The Event Dispatch Thread (EDT) is a special thread Swing uses to handle all GUI tasks.
> `() -> { new MainFrame(); }` is a Lambda expression — a short way to write code.
> `new MainFrame()` creates the main window of our application.

**Simple summary:** Main.java just starts the application and opens the main window.

---

# FILE 2 — Movie.java
### Role: Blueprint (class) for a Movie object

```java
package model;
```
> This file belongs to the `model` package (folder).

```java
public class Movie {
```
> We define a class called Movie. This is the blueprint for every movie in our system.

```java
    private String movieId;
    private String movieName;
    private String genre;
    private int duration;
    private double rating;
```
> These are the **fields** (variables) of the Movie class.
> `private` = only this class can directly access them (Encapsulation).
> `String` = text.  `int` = whole number.  `double` = decimal number.
> Every movie object will have these 5 properties.

```java
    public Movie(String movieId, String movieName, String genre, int duration, double rating) {
        this.movieId = movieId;
        this.movieName = movieName;
        ...
    }
```
> This is the **Constructor** — called when we create a new Movie object.
> `this.movieId = movieId` means: assign the value we received to this object's movieId.
> Example: `new Movie("M001", "Avengers", "Action", 181, 8.4)`

```java
    public String getMovieId() { return movieId; }
    public String getMovieName() { return movieName; }
    ...
```
> These are **Getters** — methods that return the private field values.
> Since fields are private, other classes use getters to read them.

```java
    public void setMovieName(String movieName) { this.movieName = movieName; }
    ...
```
> These are **Setters** — methods that update the private field values.
> Used when we want to update a movie's details.

```java
    @Override
    public String toString() {
        return movieId + " | " + movieName + " | " + genre + " | " + duration + " min | Rating: " + rating;
    }
```
> `toString()` converts the Movie object into a readable text string.
> `@Override` means we are replacing the default toString() from Java's Object class.
> Used when we print or display the movie.

**Simple summary:** Movie.java is a template. It says "a movie has an ID, name, genre, duration, and rating." Every movie we add creates one Movie object.

---

# FILE 3 — Customer.java
### Role: Blueprint for a Customer object

```java
    private String customerId;
    private String name;
    private String phone;
    private String email;
```
> A customer has 4 fields: ID, name, phone, email. All private (Encapsulation).

```java
    public Customer(String customerId, String name, String phone, String email) {
        this.customerId = customerId;
        ...
    }
```
> Constructor — creates a new Customer object with the given details.

```java
    public static boolean isValidPhone(String phone) {
        return phone != null && phone.matches("\\d{10}");
    }
```
> **Validation method.** Checks if the phone number is exactly 10 digits.
> `\\d{10}` is a regex (pattern): `\d` = any digit, `{10}` = exactly 10 times.
> `static` = we can call it without creating a Customer object: `Customer.isValidPhone("9876543210")`

```java
    public static boolean isValidName(String name) {
        return name != null && !name.trim().isEmpty();
    }
```
> Checks that the name is not empty or just spaces.
> `trim()` removes leading/trailing spaces. `isEmpty()` checks if string is empty.

**Simple summary:** Customer.java stores customer details and also has built-in validation to check phone and name.

---

# FILE 4 — Show.java
### Role: Blueprint for a Show (a movie playing at a specific time with seats)

```java
    private String showId;
    private Movie movie;
    private String showTime;
    private String[] seats;
    private boolean[] seatBooked;
```
> `String[] seats` is an **Array** — stores all 15 seat names (A1 to C5).
> `boolean[] seatBooked` is another array — stores true/false for each seat.
> `true` = seat is booked. `false` = seat is available.
> Both arrays have 15 elements (one per seat).

```java
    public Show(String showId, Movie movie, String showTime) {
        ...
        seats = new String[15];
        seatBooked = new boolean[15];
        String[] rows = {"A", "B", "C"};
        int index = 0;
        for (String row : rows) {
            for (int col = 1; col <= 5; col++) {
                seats[index] = row + col;
                seatBooked[index] = false;
                index++;
            }
        }
    }
```
> Constructor creates a Show and fills the seats array with: A1, A2, A3, A4, A5, B1... C5.
> Uses a nested for loop: outer loop = rows (A, B, C), inner loop = columns (1 to 5).
> All seats start as `false` (not booked).

```java
    public boolean isSeatAvailable(String seatNumber) {
        for (int i = 0; i < seats.length; i++) {
            if (seats[i].equalsIgnoreCase(seatNumber)) {
                return !seatBooked[i];
            }
        }
        return false;
    }
```
> Loops through the seats array. If the seat is found, returns `!seatBooked[i]`.
> `!seatBooked[i]` means "available = NOT booked". If booked is true, available is false.
> `equalsIgnoreCase` = case-insensitive comparison (a1 == A1).
> Returns `false` if the seat doesn't even exist.

```java
    public void bookSeat(String seatNumber) throws Exception {
        for (int i = 0; i < seats.length; i++) {
            if (seats[i].equalsIgnoreCase(seatNumber)) {
                if (seatBooked[i]) {
                    throw new Exception("Seat " + seatNumber + " is already booked!");
                }
                seatBooked[i] = true;
                return;
            }
        }
        throw new Exception("Invalid seat number: " + seatNumber);
    }
```
> Finds the seat in the array. If already booked → throws exception.
> If available → sets `seatBooked[i] = true` (marks as booked) and returns.
> If seat not found at all → throws "Invalid seat number" exception.
> `throws Exception` = this method might throw an error — caller must handle it.

```java
    public void cancelSeat(String seatNumber) {
        for (int i = 0; i < seats.length; i++) {
            if (seats[i].equalsIgnoreCase(seatNumber)) {
                seatBooked[i] = false;
                return;
            }
        }
    }
```
> Finds the seat and sets `seatBooked[i] = false` → marks it as available again.

```java
    public String getAvailableSeatsInfo() {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < seats.length; i++) {
            if (!seatBooked[i]) {
                sb.append(seats[i]).append("  ");
            }
            if ((i + 1) % 5 == 0) sb.append("\n");
        }
        return sb.toString().trim();
    }
```
> Builds a string showing only available seats.
> `StringBuilder` is used to efficiently join strings in a loop.
> `(i + 1) % 5 == 0` → after every 5 seats, add a new line (to show rows A, B, C).

```java
    public String getAllSeatsInfo() {
        ...
        if (seatBooked[i]) {
            sb.append("[").append(seats[i]).append("]");
        } else {
            sb.append(" ").append(seats[i]).append(" ");
        }
```
> Shows ALL seats. Booked seats appear in brackets like `[A1]`, free seats appear as ` A1 `.

**Simple summary:** Show.java manages a movie show — what movie, what time, and a 15-seat layout. It tracks which seats are booked using two parallel arrays.

---

# FILE 5 — Ticket.java
### Role: Blueprint for a Ticket (proof of booking)

```java
    private String ticketId;
    private Customer customer;
    private Movie movie;
    private Show show;
    private String seatNumber;
    private double price;
```
> A ticket stores references to 3 other objects: Customer, Movie, Show.
> This is called **object composition** — one object contains other objects.

```java
    public String getBillInfo() {
        return "--------------------------------\n" +
               "       MOVIE TICKET BILL\n" +
               "--------------------------------\n" +
               "Ticket ID : " + ticketId + "\n" +
               "Customer  : " + customer.getName() + "\n" +
               "Movie     : " + movie.getMovieName() + "\n" +
               "Show Time : " + show.getShowTime() + "\n" +
               "Seat      : " + seatNumber + "\n" +
               "Price     : Rs." + (int) price + "\n" +
               "--------------------------------\n" +
               "Total     : Rs." + (int) price + "\n" +
               "--------------------------------";
    }
```
> Returns a formatted bill string. This is what shows up in the popup dialog when you book.
> `(int) price` casts the double to int (removes decimals, e.g. 200.0 → 200).
> `\n` = new line character.

**Simple summary:** Ticket.java is the receipt. It holds all booking details and can generate a formatted bill.

---

# FILE 6 — SeatAlreadyBookedException.java
### Role: Custom Exception for when a seat is already taken

```java
package model;

public class SeatAlreadyBookedException extends Exception {

    public SeatAlreadyBookedException(String message) {
        super(message);
    }
}
```
> `extends Exception` = this is a custom exception that inherits from Java's Exception class.
> This is **Inheritance** in action.
> `super(message)` = calls the parent class (Exception) constructor and passes the message to it.
> When we `throw new SeatAlreadyBookedException("Seat A1 is already booked!")`, the message goes there.
> Why make a custom exception? So the GUI can catch it SEPARATELY from general errors and show a different warning message.

**Simple summary:** Just 7 lines. It's a special type of error we created specifically for "seat already booked" situations.

---

# FILE 7 — BookingSystem.java
### Role: The brain — all data + all logic lives here

```java
    private ArrayList<Movie> movies;
    private ArrayList<Customer> customers;
    private LinkedList<Ticket> bookingList;
    private HashMap<String, Ticket> tickets;
    private TreeMap<String, Show> shows;
```
> **All 5 Java Collections are declared here.** This is what the teacher will check first.
> `ArrayList<Movie>` = dynamic list of movies (can grow/shrink).
> `ArrayList<Customer>` = dynamic list of customers.
> `LinkedList<Ticket>` = ordered list of all bookings (booking sequence preserved).
> `HashMap<String, Ticket>` = key-value store. Key = Ticket ID, Value = Ticket object. Fast lookup.
> `TreeMap<String, Show>` = key-value store, but AUTOMATICALLY SORTED by key (show time).

```java
    private int movieCounter = 1;
    private int customerCounter = 1;
    private int ticketCounter = 1;
    private int showCounter = 1;
```
> Simple integer counters used to generate unique IDs: M001, M002, M003...

```java
    public BookingSystem() {
        movies = new ArrayList<>();
        customers = new ArrayList<>();
        bookingList = new LinkedList<>();
        tickets = new HashMap<>();
        shows = new TreeMap<>();
        loadSampleData();
    }
```
> Constructor — creates/initializes all 5 collections when the app starts.
> Then calls `loadSampleData()` to pre-fill the app with sample movies and shows.

---

### addMovie() method

```java
    public void addMovie(String name, String genre, int duration, double rating) {
        String id = "M" + String.format("%03d", movieCounter++);
        Movie movie = new Movie(id, name, genre, duration, rating);
        movies.add(movie);
    }
```
> `String.format("%03d", movieCounter++)` formats the counter as 3 digits: 1 → "001", so ID = "M001".
> `movieCounter++` increments after use (M001, M002, M003...).
> Creates a new Movie object and adds it to the ArrayList.

---

### updateMovie() method

```java
    public boolean updateMovie(String movieId, String name, ...) {
        for (Movie m : movies) {
            if (m.getMovieId().equalsIgnoreCase(movieId)) {
                m.setMovieName(name);
                ...
                return true;
            }
        }
        return false;
    }
```
> **For-each loop** searches the ArrayList for the movie with the matching ID.
> If found → uses setters to update fields → returns `true`.
> If not found → returns `false` (caller uses this to show an error).

---

### deleteMovie() method

```java
    public boolean deleteMovie(String movieId) {
        Movie toRemove = null;
        for (Movie m : movies) {
            if (m.getMovieId().equalsIgnoreCase(movieId)) {
                toRemove = m;
                break;
            }
        }
        if (toRemove != null) {
            movies.remove(toRemove);
            return true;
        }
        return false;
    }
```
> We can't remove while looping (causes ConcurrentModificationException).
> So we first FIND the movie and store it in `toRemove`, then remove it after the loop ends.

---

### searchMovieByName() method

```java
    public ArrayList<Movie> searchMovieByName(String name) {
        ArrayList<Movie> result = new ArrayList<>();
        for (Movie m : movies) {
            if (m.getMovieName().toLowerCase().contains(name.toLowerCase())) {
                result.add(m);
            }
        }
        return result;
    }
```
> Partial search — finds movies whose name **contains** the search word.
> `.toLowerCase()` makes search case-insensitive.
> Returns a new ArrayList with all matching movies.

---

### getMoviesSortedByName() method

```java
    public ArrayList<Movie> getMoviesSortedByName() {
        ArrayList<Movie> sorted = new ArrayList<>(movies);
        Collections.sort(sorted, Comparator.comparing(Movie::getMovieName));
        return sorted;
    }
```
> Creates a copy of the movies list (we don't want to change the original order).
> `Collections.sort()` sorts the list using a Comparator.
> `Comparator.comparing(Movie::getMovieName)` = sort by movie name alphabetically.
> `Movie::getMovieName` is a **Method Reference** — a short way to pass a method.

---

### getMoviesSortedByRating() method

```java
    public ArrayList<Movie> getMoviesSortedByRating() {
        ArrayList<Movie> sorted = new ArrayList<>(movies);
        sorted.sort((m1, m2) -> Double.compare(m2.getRating(), m1.getRating()));
        return sorted;
    }
```
> `(m1, m2) -> Double.compare(m2.getRating(), m1.getRating())` is a **Lambda + Comparator**.
> `m2 vs m1` (not m1 vs m2) means DESCENDING order (highest rating first).

---

### addShow() method

```java
    public void addShow(String movieId, String showTime) {
        Movie movie = searchMovie(movieId);
        if (movie == null) return;

        String showId = "S" + String.format("%03d", showCounter++);
        Show show = new Show(showId, movie, showTime);
        shows.put(showTime + "_" + showId, show);
    }
```
> Finds the Movie object by ID. If not found, exits immediately.
> Creates a Show object and adds it to the **TreeMap**.
> Key = `showTime + "_" + showId` (e.g. `"10:00 AM_S001"`).
> TreeMap automatically keeps entries sorted by this key → shows appear in time order.

---

### bookTicket() method (most important)

```java
    public Ticket bookTicket(String customerName, String phone, String email,
                              String showId, String seatNumber)
            throws SeatAlreadyBookedException, Exception {
```
> `throws SeatAlreadyBookedException, Exception` = this method can throw two types of errors.
> Callers (BookingPanel) MUST handle them with try-catch.

```java
        if (!Customer.isValidName(customerName)) {
            throw new Exception("Customer name cannot be empty.");
        }
        if (!Customer.isValidPhone(phone)) {
            throw new Exception("Phone number must be 10 digits.");
        }
```
> **Validation** — checks inputs before doing anything. Throws exception if invalid.

```java
        Show show = searchShow(showId);
        if (show == null) {
            throw new Exception("Show not found: " + showId);
        }
```
> Find the show. If it doesn't exist, throw an error.

```java
        if (!show.isSeatAvailable(seatNumber)) {
            ...
            throw new SeatAlreadyBookedException("Seat " + seatNumber + " is already booked!");
        }
```
> Check seat availability. Throws **our custom exception** if seat is taken.

```java
        String customerId = addCustomer(customerName, phone, email);
        Customer customer = searchCustomer(customerId);
        show.bookSeat(seatNumber);
```
> Register the customer (auto-generate ID). Then actually book the seat in the show.

```java
        String ticketId = "T" + String.format("%03d", ticketCounter++);
        double price = 200.0;
        Ticket ticket = new Ticket(ticketId, customer, show.getMovie(), show, seatNumber, price);

        tickets.put(ticketId, ticket);
        bookingList.add(ticket);

        return ticket;
    }
```
> Create the Ticket object. Store it in BOTH:
> - `HashMap` (tickets) → for fast search by ticket ID.
> - `LinkedList` (bookingList) → to preserve booking order.
> Return the ticket so the GUI can show the bill.

---

### cancelTicket() method

```java
    public boolean cancelTicket(String ticketId) {
        Ticket ticket = tickets.get(ticketId);
        if (ticket == null) return false;

        ticket.getShow().cancelSeat(ticket.getSeatNumber());
        tickets.remove(ticketId);
        bookingList.remove(ticket);
        return true;
    }
```
> `tickets.get(ticketId)` — **HashMap lookup** (O(1) speed — very fast).
> Then frees the seat, removes from HashMap, removes from LinkedList.
> Returns `true` if cancelled, `false` if ticket not found.

**Simple summary:** BookingSystem.java is the heart. It holds all 5 collections and all the logic. The GUI just calls its methods — it doesn't know how the logic works inside.

---

# FILE 8 — MainFrame.java
### Role: The main application window (JFrame)

```java
public class MainFrame extends JFrame {
```
> `extends JFrame` = MainFrame **inherits** from JFrame (Inheritance).
> JFrame is Java Swing's main window class. By extending it, our class IS a window.

```java
    private BookingSystem bookingSystem;
    private MoviePanel moviePanel;
    private BookingPanel bookingPanel;
    private TicketPanel ticketPanel;
```
> MainFrame holds references to: one BookingSystem (shared by all panels) and the 3 panel objects.

```java
    public MainFrame() {
        bookingSystem = new BookingSystem();
```
> Constructor — creates ONE BookingSystem object. This same object is shared with all 3 panels.
> This is important: all panels share the SAME data. When BookingPanel adds a ticket, TicketPanel sees it.

```java
        setTitle("Movie Ticket Booking System");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(900, 600);
        setLocationRelativeTo(null);
        setLayout(new BorderLayout());
```
> Standard JFrame setup:
> - Title shown in the title bar.
> - `EXIT_ON_CLOSE` = close the app when the X button is clicked.
> - `setSize(900, 600)` = window is 900px wide, 600px tall.
> - `setLocationRelativeTo(null)` = centers the window on the screen.
> - `BorderLayout` divides the window into: NORTH, SOUTH, EAST, WEST, CENTER.

```java
        JLabel header = new JLabel("  Movie Ticket Booking System", JLabel.LEFT);
        header.setFont(new Font("Arial", Font.BOLD, 20));
        header.setOpaque(true);
        header.setBackground(new Color(30, 60, 114));
        header.setForeground(Color.WHITE);
        header.setPreferredSize(new Dimension(900, 50));
        add(header, BorderLayout.NORTH);
```
> Creates a blue header bar at the top of the window.
> `setOpaque(true)` = must be true for background color to show.
> `new Color(30, 60, 114)` = dark blue (RGB values).
> `add(header, BorderLayout.NORTH)` = places it at the top of the BorderLayout.

```java
        JTabbedPane tabbedPane = new JTabbedPane();
        tabbedPane.addTab("  Movies  ", moviePanel);
        tabbedPane.addTab("  Book Ticket  ", bookingPanel);
        tabbedPane.addTab("  My Tickets  ", ticketPanel);
```
> `JTabbedPane` creates the 3 clickable tabs at the top.
> Each tab shows one of our panels when clicked.

```java
        tabbedPane.addChangeListener(e -> {
            int selected = tabbedPane.getSelectedIndex();
            if (selected == 0) moviePanel.refreshTable();
            if (selected == 1) bookingPanel.refreshMovies();
            if (selected == 2) ticketPanel.refreshTable();
        });
```
> `ChangeListener` fires every time the user clicks a different tab.
> We refresh the selected panel so it shows updated data.
> Example: if you add a movie and switch to Book Ticket, the new movie appears in the dropdown.

```java
        JButton btnExit = new JButton("Exit");
        btnExit.addActionListener(e -> {
            int confirm = JOptionPane.showConfirmDialog(...);
            if (confirm == JOptionPane.YES_OPTION) System.exit(0);
        });
```
> Exit button with a confirmation dialog. `System.exit(0)` closes the program.
> `addActionListener` = event handling — tells Java what to do when button is clicked.

**Simple summary:** MainFrame is the outer shell. It creates the window, adds the blue header, sets up 3 tabs, and connects all panels to the same BookingSystem.

---

# FILE 9 — MoviePanel.java
### Role: The "Movies" tab — Add, Update, Delete, Search, Sort movies

```java
public class MoviePanel extends JPanel {
```
> `extends JPanel` = this class IS a panel (Inheritance). We place it inside the JTabbedPane.

```java
    private JTextField txtMovieName, txtGenre, txtDuration, txtRating, txtSearchId;
    private JTable movieTable;
    private DefaultTableModel tableModel;
```
> All the input fields are declared here.
> `JTable` = displays data in rows and columns.
> `DefaultTableModel` = the data model behind the JTable (holds the actual cell data).

```java
    public MoviePanel(BookingSystem bookingSystem) {
        this.bookingSystem = bookingSystem;
        setLayout(new BorderLayout(10, 10));
        ...
        add(createFormPanel(), BorderLayout.NORTH);
        add(createTablePanel(), BorderLayout.CENTER);
        add(createButtonPanel(), BorderLayout.SOUTH);
        refreshTable();
    }
```
> Constructor splits the panel into 3 zones using BorderLayout:
> - NORTH = input form fields.
> - CENTER = the movie table.
> - SOUTH = action buttons.

```java
    private JScrollPane createTablePanel() {
        String[] columns = {"Movie ID", "Movie Name", "Genre", "Duration (min)", "Rating"};
        tableModel = new DefaultTableModel(columns, 0) {
            public boolean isCellEditable(int r, int c) { return false; }
        };
        movieTable = new JTable(tableModel);
```
> Creates the table with 5 columns.
> `isCellEditable returns false` = users can't edit cells directly in the table (read-only).
> `0` = start with 0 rows (data loaded later by refreshTable).

```java
        movieTable.getSelectionModel().addListSelectionListener(e -> {
            int row = movieTable.getSelectedRow();
            if (row >= 0) {
                txtSearchId.setText((String) tableModel.getValueAt(row, 0));
            }
        });
```
> When a row is clicked in the table, the Movie ID is auto-filled in the search field.
> `getSelectedRow()` = returns the row number clicked (-1 if nothing selected).
> `tableModel.getValueAt(row, 0)` = gets the value in column 0 (Movie ID) of that row.

```java
    private void addMovie() {
        try {
            String name = txtMovieName.getText().trim();
            ...
            if (name.isEmpty()) throw new Exception("Movie name cannot be empty.");
            ...
            int duration = Integer.parseInt(durStr);
            double rating = Double.parseDouble(ratingStr);
            ...
            bookingSystem.addMovie(name, genre, duration, rating);
            refreshTable();
            clearForm();
            JOptionPane.showMessageDialog(this, "Movie added successfully!", ...);
        } catch (NumberFormatException e) {
            JOptionPane.showMessageDialog(this, "Duration and Rating must be valid numbers.", ...);
        } catch (Exception e) {
            JOptionPane.showMessageDialog(this, e.getMessage(), ...);
        }
    }
```
> Full try-catch block.
> `Integer.parseInt()` converts text to int — throws `NumberFormatException` if text is not a number.
> `Double.parseDouble()` converts text to double.
> If any validation fails → exception is thrown → caught by catch → error shown in popup.
> If all good → calls bookingSystem.addMovie() → refreshes table → clears form.

```java
    private void addShowForMovie() {
        String movieId = txtSearchId.getText().trim();
        ...
        String showTime = JOptionPane.showInputDialog(this, "Enter show time...");
        ...
        bookingSystem.addShow(movieId, showTime.trim());
    }
```
> The orange "Add Show for Movie" button's logic.
> `JOptionPane.showInputDialog()` shows a small popup where user types the show time.
> Calls `bookingSystem.addShow()` to create the show.

```java
    public void refreshTable() {
        tableModel.setRowCount(0);
        for (Movie m : bookingSystem.getMovies()) {
            tableModel.addRow(new Object[]{m.getMovieId(), m.getMovieName(), m.getGenre(), m.getDuration(), m.getRating()});
        }
    }
```
> `setRowCount(0)` = clears the table.
> Then loops through all movies and adds each one as a new row.
> Called after every Add/Update/Delete/Sort to keep the table up to date.

**Simple summary:** MoviePanel is the Movies tab. It provides input fields and buttons to manage movies and shows the list in a table.

---

# FILE 10 — BookingPanel.java
### Role: The "Book Ticket" tab — select movie, show, seat, enter details, book

```java
    private JComboBox<String> cmbMovie, cmbShow;
    private JTextField txtCustomerName, txtPhone, txtEmail, txtSeat;
    private JTextArea txtAvailableSeats;
```
> `JComboBox` = dropdown selector. One for movie, one for show.
> `JTextArea` = multi-line text area showing available seats.

```java
    cmbMovie.addActionListener(e -> loadShowsForSelectedMovie());
```
> **Event handling** — when the movie dropdown selection changes, auto-load that movie's shows.

```java
    private void loadShowsForSelectedMovie() {
        cmbShow.removeAllItems();
        if (cmbMovie.getSelectedItem() == null) return;

        String selected = (String) cmbMovie.getSelectedItem();
        String movieId = selected.split(" - ")[0];

        ArrayList<Show> movieShows = bookingSystem.getShowsForMovie(movieId);
        for (Show s : movieShows) {
            cmbShow.addItem(s.getShowId() + " - " + s.getShowTime());
        }
        viewSeats();
    }
```
> Clears the show dropdown first. Then:
> `selected.split(" - ")[0]` = extract just the Movie ID from text like "M001 - Avengers".
> Calls `bookingSystem.getShowsForMovie(movieId)` → gets all shows for that movie.
> Adds each show to the show dropdown. Then calls `viewSeats()` to show the seat map.

```java
    private void viewSeats() {
        if (cmbShow.getSelectedItem() == null) {
            txtAvailableSeats.setText("No shows available.");
            return;
        }
        String selected = (String) cmbShow.getSelectedItem();
        String showId = selected.split(" - ")[0];
        txtAvailableSeats.setText(bookingSystem.getAvailableSeats(showId));
    }
```
> Extracts Show ID from the dropdown. Gets seat map from BookingSystem. Displays it in the text area.

```java
    private void bookTicket() {
        try {
            ...
            String showId = showSelected.split(" - ")[0];
            String seat = txtSeat.getText().trim().toUpperCase();
            ...
            Ticket ticket = bookingSystem.bookTicket(name, phone, email, showId, seat);
            JOptionPane.showMessageDialog(this, "Ticket booked successfully!\n\n" + ticket.getBillInfo(), ...);
            viewSeats();
            clearForm();

        } catch (SeatAlreadyBookedException e) {
            JOptionPane.showMessageDialog(this, e.getMessage(), "Seat Unavailable", JOptionPane.WARNING_MESSAGE);
        } catch (Exception e) {
            JOptionPane.showMessageDialog(this, e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
        }
    }
```
> `.toUpperCase()` = converts seat input to uppercase so "a1" becomes "A1".
> Calls `bookingSystem.bookTicket()` — which can throw two exception types.
> **Two separate catch blocks** — `SeatAlreadyBookedException` shows a WARNING, general Exception shows ERROR.
> After booking → shows the bill popup → refreshes seat map → clears form.

```java
    public void refreshMovies() {
        cmbMovie.removeAllItems();
        for (Movie m : bookingSystem.getMovies()) {
            cmbMovie.addItem(m.getMovieId() + " - " + m.getMovieName());
        }
        loadShowsForSelectedMovie();
    }
```
> Clears and repopulates the movie dropdown. Called when the tab is opened.
> This is how newly added movies appear in the booking dropdown.

**Simple summary:** BookingPanel collects customer info, lets them pick a movie/show/seat, and books the ticket by calling bookingSystem.bookTicket().

---

# FILE 11 — TicketPanel.java
### Role: The "My Tickets" tab — search, view, cancel tickets

```java
    private JTextField txtTicketId;
    private JTable ticketTable;
    private DefaultTableModel tableModel;
```
> Simple setup: a text field for Ticket ID input, and a table to display tickets.

```java
    private void searchTicket() {
        String ticketId = txtTicketId.getText().trim();
        ...
        Ticket ticket = bookingSystem.searchTicket(ticketId);
        if (ticket == null) {
            JOptionPane.showMessageDialog(this, "Ticket not found: " + ticketId, ...);
            return;
        }
        tableModel.setRowCount(0);
        tableModel.addRow(new Object[]{
                ticket.getTicketId(),
                ticket.getCustomer().getName(),
                ...
        });
    }
```
> `bookingSystem.searchTicket(ticketId)` uses **HashMap.get()** — returns null if not found.
> If found → clears the table and shows just that one ticket.

```java
    private void cancelTicket() {
        ...
        int confirm = JOptionPane.showConfirmDialog(this,
                "Cancel ticket " + ticketId + " for " + ticket.getCustomer().getName() + "?",
                "Confirm Cancellation", JOptionPane.YES_NO_OPTION);

        if (confirm == JOptionPane.YES_OPTION) {
            boolean cancelled = bookingSystem.cancelTicket(ticketId);
            if (cancelled) {
                refreshTable();
                JOptionPane.showMessageDialog(this, "Ticket cancelled. Seat is now available.", ...);
            }
        }
    }
```
> Shows a YES/NO confirmation dialog before cancelling.
> `JOptionPane.YES_OPTION` = 0 (the "Yes" button was clicked).
> Calls `bookingSystem.cancelTicket()` which frees the seat and removes from both collections.

```java
    private void viewBill() {
        ...
        Ticket ticket = bookingSystem.searchTicket(ticketId);
        ...
        JOptionPane.showMessageDialog(this, ticket.getBillInfo(), "Ticket Bill", ...);
    }
```
> Searches for the ticket and calls `getBillInfo()` to get the formatted bill string.
> Shows it in a dialog box.

```java
    public void refreshTable() {
        tableModel.setRowCount(0);
        LinkedList<Ticket> bookingList = bookingSystem.getBookingList();
        for (Ticket t : bookingList) {
            tableModel.addRow(new Object[]{...});
        }
    }
```
> Iterates over the **LinkedList** (which preserves booking order).
> Adds each ticket as a row in the table.

**Simple summary:** TicketPanel shows all booked tickets, lets you search by ID, cancel, and view the bill.

---

# COMPLETE PROJECT DATA FLOW

```
User opens app
      ↓
Main.java → creates MainFrame
      ↓
MainFrame → creates BookingSystem (loads sample data)
          → creates MoviePanel, BookingPanel, TicketPanel
          → shows window with 3 tabs
      ↓
User clicks "Movies" tab
  → MoviePanel.refreshTable() → shows all movies from ArrayList
      ↓
User adds a movie
  → MoviePanel.addMovie() → validates → BookingSystem.addMovie()
    → creates Movie object → adds to ArrayList → table refreshes
      ↓
User adds a show for that movie
  → MoviePanel.addShowForMovie() → BookingSystem.addShow()
    → creates Show object → puts in TreeMap (auto-sorted)
      ↓
User clicks "Book Ticket" tab
  → BookingPanel.refreshMovies() → fills movie dropdown from ArrayList
  → User selects movie → loadShowsForSelectedMovie()
    → getShowsForMovie() → fills show dropdown
  → User clicks "View Seats" → viewSeats()
    → getAvailableSeats() → getAllSeatsInfo() → shows seat map
  → User fills details + seat → clicks "Book Ticket"
    → bookTicket() → validates → registers customer
    → books seat in Show → creates Ticket
    → stores in HashMap + LinkedList → returns ticket
    → GUI shows bill popup
      ↓
User clicks "My Tickets" tab
  → TicketPanel.refreshTable() → iterates LinkedList → fills table
  → User types Ticket ID → searchTicket() → HashMap.get() → shows ticket
  → User cancels → cancelTicket()
    → frees seat in Show → removes from HashMap + LinkedList
```

---

# QUICK REFERENCE — Where Is Each Concept

| Concept | File | What to show |
|---------|------|-------------|
| Array | Show.java | `String[] seats` and `boolean[] seatBooked` |
| ArrayList | BookingSystem.java | `ArrayList<Movie> movies` field |
| LinkedList | BookingSystem.java | `LinkedList<Ticket> bookingList` field |
| HashMap | BookingSystem.java | `HashMap<String, Ticket> tickets` field |
| TreeMap | BookingSystem.java | `TreeMap<String, Show> shows` field |
| Constructor | Movie.java | `public Movie(...)` method |
| Encapsulation | Movie.java | private fields + getters/setters |
| Inheritance | SeatAlreadyBookedException.java | `extends Exception` |
| Inheritance (GUI) | MainFrame.java | `extends JFrame` |
| Custom Exception | SeatAlreadyBookedException.java | the whole file |
| Exception Handling | BookingSystem.java | `bookTicket()` try-catch |
| Validation | Customer.java | `isValidPhone()`, `isValidName()` |
| toString() | Movie.java | `@Override public String toString()` |
| Collections.sort() | BookingSystem.java | `getMoviesSortedByName()` |
| Comparator + Lambda | BookingSystem.java | `getMoviesSortedByRating()` |
| Event Handling | BookingPanel.java | `btnBook.addActionListener(e -> bookTicket())` |
| JTable | MoviePanel.java | `movieTable` + `DefaultTableModel` |
| JComboBox | BookingPanel.java | `cmbMovie`, `cmbShow` |
| JOptionPane | All GUI files | popups for errors/success/bills |
| JTabbedPane | MainFrame.java | the 3-tab layout |
