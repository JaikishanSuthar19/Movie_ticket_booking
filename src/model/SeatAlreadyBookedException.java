package model;

// Custom exception for seat already booked scenario
public class SeatAlreadyBookedException extends Exception {

    public SeatAlreadyBookedException(String message) {
        super(message);
    }
}
