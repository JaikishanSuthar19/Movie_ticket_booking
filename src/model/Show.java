package model;

public class Show {

    private String showId;
    private Movie movie;
    private String showTime;

    // Array to store cinema seats: 3 rows x 5 cols = 15 seats
    private String[] seats;
    private boolean[] seatBooked;

    public Show(String showId, Movie movie, String showTime) {
        this.showId = showId;
        this.movie = movie;
        this.showTime = showTime;

        // Initialize seat layout: A1-A5, B1-B5, C1-C5
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

    // Check if a seat is available
    public boolean isSeatAvailable(String seatNumber) {
        for (int i = 0; i < seats.length; i++) {
            if (seats[i].equalsIgnoreCase(seatNumber)) {
                return !seatBooked[i];
            }
        }
        return false; // seat doesn't exist
    }

    // Book a seat
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

    // Cancel a seat
    public void cancelSeat(String seatNumber) {
        for (int i = 0; i < seats.length; i++) {
            if (seats[i].equalsIgnoreCase(seatNumber)) {
                seatBooked[i] = false;
                return;
            }
        }
    }

    // Get list of available seats as a string
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

    // Get all seats with status
    public String getAllSeatsInfo() {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < seats.length; i++) {
            if (seatBooked[i]) {
                sb.append("[").append(seats[i]).append("]");
            } else {
                sb.append(" ").append(seats[i]).append(" ");
            }
            sb.append("  ");
            if ((i + 1) % 5 == 0) sb.append("\n");
        }
        return sb.toString();
    }

    // Getters
    public String getShowId() { return showId; }
    public Movie getMovie() { return movie; }
    public String getShowTime() { return showTime; }
    public String[] getSeats() { return seats; }

    @Override
    public String toString() {
        return showId + " | " + movie.getMovieName() + " | " + showTime;
    }
}
