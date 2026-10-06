package model;

public class Ticket {

    private String ticketId;
    private Customer customer;
    private Movie movie;
    private Show show;
    private String seatNumber;
    private double price;

    public Ticket(String ticketId, Customer customer, Movie movie, Show show, String seatNumber, double price) {
        this.ticketId = ticketId;
        this.customer = customer;
        this.movie = movie;
        this.show = show;
        this.seatNumber = seatNumber;
        this.price = price;
    }

    // Getters
    public String getTicketId() { return ticketId; }
    public Customer getCustomer() { return customer; }
    public Movie getMovie() { return movie; }
    public Show getShow() { return show; }
    public String getSeatNumber() { return seatNumber; }
    public double getPrice() { return price; }

    // Get bill as formatted string
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

    @Override
    public String toString() {
        return ticketId + " | " + customer.getName() + " | " + movie.getMovieName() +
               " | " + show.getShowTime() + " | Seat: " + seatNumber + " | Rs." + (int) price;
    }
}
