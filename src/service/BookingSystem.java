package service;

import model.*;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.TreeMap;

public class BookingSystem {

    // ArrayList to store movies
    private ArrayList<Movie> movies;

    // ArrayList to store customers
    private ArrayList<Customer> customers;

    // LinkedList to maintain booking list (booking order preserved)
    private LinkedList<Ticket> bookingList;

    // HashMap to store tickets by Ticket ID for fast lookup
    private HashMap<String, Ticket> tickets;

    // TreeMap to store shows sorted by show time automatically
    private TreeMap<String, Show> shows;

    // Counters for generating IDs
    private int movieCounter = 1;
    private int customerCounter = 1;
    private int ticketCounter = 1;
    private int showCounter = 1;

    public BookingSystem() {
        movies = new ArrayList<>();
        customers = new ArrayList<>();
        bookingList = new LinkedList<>();
        tickets = new HashMap<>();
        shows = new TreeMap<>();

        // Load sample data when app starts
        loadSampleData();
    }

    // ===================== SAMPLE DATA =====================

    private void loadSampleData() {
        // Add sample movies
        addMovie("Avengers: Endgame", "Action", 181, 8.4);
        addMovie("Avatar", "Sci-Fi", 162, 7.8);
        addMovie("Inception", "Thriller", 148, 8.8);
        addMovie("Interstellar", "Sci-Fi", 169, 8.6);

        // Add sample shows
        addShow("M001", "10:00 AM");
        addShow("M002", "01:00 PM");
        addShow("M001", "06:00 PM");
        addShow("M003", "09:00 PM");
    }

    // ===================== MOVIE METHODS =====================

    public void addMovie(String name, String genre, int duration, double rating) {
        String id = "M" + String.format("%03d", movieCounter++);
        Movie movie = new Movie(id, name, genre, duration, rating);
        movies.add(movie);
    }

    public boolean updateMovie(String movieId, String name, String genre, int duration, double rating) {
        for (Movie m : movies) {
            if (m.getMovieId().equalsIgnoreCase(movieId)) {
                m.setMovieName(name);
                m.setGenre(genre);
                m.setDuration(duration);
                m.setRating(rating);
                return true;
            }
        }
        return false;
    }

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

    public Movie searchMovie(String movieId) {
        for (Movie m : movies) {
            if (m.getMovieId().equalsIgnoreCase(movieId)) {
                return m;
            }
        }
        return null;
    }

    public ArrayList<Movie> searchMovieByName(String name) {
        ArrayList<Movie> result = new ArrayList<>();
        for (Movie m : movies) {
            if (m.getMovieName().toLowerCase().contains(name.toLowerCase())) {
                result.add(m);
            }
        }
        return result;
    }

    public ArrayList<Movie> getMoviesSortedByName() {
        ArrayList<Movie> sorted = new ArrayList<>(movies);
        Collections.sort(sorted, Comparator.comparing(Movie::getMovieName));
        return sorted;
    }

    public ArrayList<Movie> getMoviesSortedByRating() {
        ArrayList<Movie> sorted = new ArrayList<>(movies);
        sorted.sort((m1, m2) -> Double.compare(m2.getRating(), m1.getRating())); // highest first
        return sorted;
    }

    public ArrayList<Movie> getMovies() {
        return movies;
    }

    // ===================== CUSTOMER METHODS =====================

    public String addCustomer(String name, String phone, String email) {
        String id = "C" + String.format("%03d", customerCounter++);
        Customer customer = new Customer(id, name, phone, email);
        customers.add(customer);
        return id;
    }

    public Customer searchCustomer(String customerId) {
        for (Customer c : customers) {
            if (c.getCustomerId().equalsIgnoreCase(customerId)) {
                return c;
            }
        }
        return null;
    }

    public ArrayList<Customer> getCustomers() {
        return customers;
    }

    // ===================== SHOW METHODS =====================

    public void addShow(String movieId, String showTime) {
        Movie movie = searchMovie(movieId);
        if (movie == null) return;

        String showId = "S" + String.format("%03d", showCounter++);
        Show show = new Show(showId, movie, showTime);
        // TreeMap key = showTime + showId so same-time shows are sorted predictably
        shows.put(showTime + "_" + showId, show);
    }

    public Show searchShow(String showId) {
        for (Show s : shows.values()) {
            if (s.getShowId().equalsIgnoreCase(showId)) {
                return s;
            }
        }
        return null;
    }

    public TreeMap<String, Show> getShows() {
        return shows;
    }

    public ArrayList<Show> getShowsForMovie(String movieId) {
        ArrayList<Show> result = new ArrayList<>();
        for (Show s : shows.values()) {
            if (s.getMovie().getMovieId().equalsIgnoreCase(movieId)) {
                result.add(s);
            }
        }
        return result;
    }

    // ===================== TICKET / BOOKING METHODS =====================

    public Ticket bookTicket(String customerName, String phone, String email,
                              String showId, String seatNumber)
            throws SeatAlreadyBookedException, Exception {

        // Validate customer info
        if (!Customer.isValidName(customerName)) {
            throw new Exception("Customer name cannot be empty.");
        }
        if (!Customer.isValidPhone(phone)) {
            throw new Exception("Phone number must be 10 digits.");
        }

        // Find the show
        Show show = searchShow(showId);
        if (show == null) {
            throw new Exception("Show not found: " + showId);
        }

        // Check seat availability
        if (!show.isSeatAvailable(seatNumber)) {
            // Check if it even exists
            boolean exists = false;
            for (String s : show.getSeats()) {
                if (s.equalsIgnoreCase(seatNumber)) { exists = true; break; }
            }
            if (!exists) throw new Exception("Invalid seat number: " + seatNumber);
            throw new SeatAlreadyBookedException("Seat " + seatNumber + " is already booked!");
        }

        // Register customer
        String customerId = addCustomer(customerName, phone, email);
        Customer customer = searchCustomer(customerId);

        // Book the seat in the show
        show.bookSeat(seatNumber);

        // Create ticket
        String ticketId = "T" + String.format("%03d", ticketCounter++);
        double price = 200.0; // Rs. 200 per ticket
        Ticket ticket = new Ticket(ticketId, customer, show.getMovie(), show, seatNumber, price);

        // Store in HashMap (fast lookup by ID) and LinkedList (booking order)
        tickets.put(ticketId, ticket);
        bookingList.add(ticket);

        return ticket;
    }

    public Ticket searchTicket(String ticketId) {
        return tickets.get(ticketId); // HashMap lookup
    }

    public boolean cancelTicket(String ticketId) {
        Ticket ticket = tickets.get(ticketId);
        if (ticket == null) return false;

        // Free the seat
        ticket.getShow().cancelSeat(ticket.getSeatNumber());

        // Remove from HashMap and LinkedList
        tickets.remove(ticketId);
        bookingList.remove(ticket);
        return true;
    }

    public LinkedList<Ticket> getBookingList() {
        return bookingList;
    }

    public HashMap<String, Ticket> getTickets() {
        return tickets;
    }

    public String getAvailableSeats(String showId) {
        Show show = searchShow(showId);
        if (show == null) return "Show not found.";
        return show.getAllSeatsInfo();
    }
}
