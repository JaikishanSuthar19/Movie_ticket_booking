package model;

public class Movie {

    private String movieId;
    private String movieName;
    private String genre;
    private int duration; // in minutes
    private double rating;

    public Movie(String movieId, String movieName, String genre, int duration, double rating) {
        this.movieId = movieId;
        this.movieName = movieName;
        this.genre = genre;
        this.duration = duration;
        this.rating = rating;
    }

    // Getters
    public String getMovieId() { return movieId; }
    public String getMovieName() { return movieName; }
    public String getGenre() { return genre; }
    public int getDuration() { return duration; }
    public double getRating() { return rating; }

    // Setters
    public void setMovieName(String movieName) { this.movieName = movieName; }
    public void setGenre(String genre) { this.genre = genre; }
    public void setDuration(int duration) { this.duration = duration; }
    public void setRating(double rating) { this.rating = rating; }

    @Override
    public String toString() {
        return movieId + " | " + movieName + " | " + genre + " | " + duration + " min | Rating: " + rating;
    }
}
