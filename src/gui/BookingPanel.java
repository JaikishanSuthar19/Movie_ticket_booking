package gui;

import model.*;
import service.BookingSystem;

import javax.swing.*;
import java.awt.*;
import java.util.ArrayList;
import java.util.TreeMap;

public class BookingPanel extends JPanel {

    private BookingSystem bookingSystem;

    private JComboBox<String> cmbMovie, cmbShow;
    private JTextField txtCustomerName, txtPhone, txtEmail, txtSeat;
    private JTextArea txtAvailableSeats;

    public BookingPanel(BookingSystem bookingSystem) {
        this.bookingSystem = bookingSystem;
        setLayout(new BorderLayout(10, 10));
        setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        setBackground(new Color(245, 248, 255));

        add(createFormPanel(), BorderLayout.CENTER);
        add(createButtonPanel(), BorderLayout.SOUTH);
    }

    private JPanel createFormPanel() {
        JPanel mainPanel = new JPanel(new GridLayout(1, 2, 10, 0));
        mainPanel.setBackground(new Color(245, 248, 255));

        // Left panel: booking form
        JPanel formPanel = new JPanel(new GridLayout(8, 2, 8, 8));
        formPanel.setBackground(new Color(245, 248, 255));
        formPanel.setBorder(BorderFactory.createTitledBorder("Booking Form"));

        cmbMovie = new JComboBox<>();
        cmbShow = new JComboBox<>();
        txtCustomerName = new JTextField();
        txtPhone = new JTextField();
        txtEmail = new JTextField();
        txtSeat = new JTextField();

        // Populate movies
        for (Movie m : bookingSystem.getMovies()) {
            cmbMovie.addItem(m.getMovieId() + " - " + m.getMovieName());
        }

        // When movie changes, update shows
        cmbMovie.addActionListener(e -> loadShowsForSelectedMovie());

        formPanel.add(new JLabel("Select Movie:"));
        formPanel.add(cmbMovie);
        formPanel.add(new JLabel("Select Show:"));
        formPanel.add(cmbShow);
        formPanel.add(new JLabel("Customer Name:"));
        formPanel.add(txtCustomerName);
        formPanel.add(new JLabel("Phone (10 digits):"));
        formPanel.add(txtPhone);
        formPanel.add(new JLabel("Email:"));
        formPanel.add(txtEmail);
        formPanel.add(new JLabel("Seat Number (e.g. A1):"));
        formPanel.add(txtSeat);
        formPanel.add(new JLabel(""));
        formPanel.add(new JLabel(""));
        formPanel.add(new JLabel(""));
        formPanel.add(new JLabel(""));

        // Right panel: available seats
        JPanel seatPanel = new JPanel(new BorderLayout());
        seatPanel.setBackground(new Color(245, 248, 255));
        seatPanel.setBorder(BorderFactory.createTitledBorder("Available Seats (booked shown as [X1])"));

        txtAvailableSeats = new JTextArea();
        txtAvailableSeats.setEditable(false);
        txtAvailableSeats.setFont(new Font("Monospaced", Font.PLAIN, 14));
        txtAvailableSeats.setBackground(new Color(230, 240, 255));

        JButton btnViewSeats = new JButton("View Seats");
        styleButton(btnViewSeats, new Color(23, 162, 184));
        btnViewSeats.addActionListener(e -> viewSeats());

        seatPanel.add(new JScrollPane(txtAvailableSeats), BorderLayout.CENTER);
        seatPanel.add(btnViewSeats, BorderLayout.SOUTH);

        mainPanel.add(formPanel);
        mainPanel.add(seatPanel);

        // Load initial shows
        loadShowsForSelectedMovie();

        return mainPanel;
    }

    private JPanel createButtonPanel() {
        JPanel panel = new JPanel(new FlowLayout(FlowLayout.CENTER, 10, 5));
        panel.setBackground(new Color(245, 248, 255));

        JButton btnBook = new JButton("Book Ticket");
        JButton btnClear = new JButton("Clear");
        JButton btnRefresh = new JButton("Refresh Movies");

        styleButton(btnBook, new Color(40, 167, 69));
        styleButton(btnClear, new Color(108, 117, 125));
        styleButton(btnRefresh, new Color(0, 123, 255));

        btnBook.addActionListener(e -> bookTicket());
        btnClear.addActionListener(e -> clearForm());
        btnRefresh.addActionListener(e -> refreshMovies());

        panel.add(btnBook);
        panel.add(btnClear);
        panel.add(btnRefresh);

        return panel;
    }

    private void styleButton(JButton btn, Color color) {
        btn.setBackground(color);
        btn.setForeground(Color.WHITE);
        btn.setFocusPainted(false);
        btn.setOpaque(true);
        btn.setBorderPainted(false);
        btn.setFont(new Font("Arial", Font.BOLD, 12));
        btn.setPreferredSize(new Dimension(140, 32));
    }

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

    private void viewSeats() {
        if (cmbShow.getSelectedItem() == null) {
            txtAvailableSeats.setText("No shows available.");
            return;
        }
        String selected = (String) cmbShow.getSelectedItem();
        String showId = selected.split(" - ")[0];
        txtAvailableSeats.setText(bookingSystem.getAvailableSeats(showId));
    }

    private void bookTicket() {
        try {
            if (cmbMovie.getSelectedItem() == null) throw new Exception("Please select a movie.");
            if (cmbShow.getSelectedItem() == null) throw new Exception("No show available for selected movie.");

            String showSelected = (String) cmbShow.getSelectedItem();
            String showId = showSelected.split(" - ")[0];

            String name = txtCustomerName.getText().trim();
            String phone = txtPhone.getText().trim();
            String email = txtEmail.getText().trim();
            String seat = txtSeat.getText().trim().toUpperCase();

            if (seat.isEmpty()) throw new Exception("Please enter a seat number.");

            Ticket ticket = bookingSystem.bookTicket(name, phone, email, showId, seat);

            // Show bill
            JOptionPane.showMessageDialog(this,
                    "Ticket booked successfully!\n\n" + ticket.getBillInfo(),
                    "Booking Confirmed",
                    JOptionPane.INFORMATION_MESSAGE);

            viewSeats(); // refresh seat view
            clearForm();

        } catch (SeatAlreadyBookedException e) {
            JOptionPane.showMessageDialog(this, e.getMessage(), "Seat Unavailable", JOptionPane.WARNING_MESSAGE);
        } catch (Exception e) {
            JOptionPane.showMessageDialog(this, e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    public void refreshMovies() {
        cmbMovie.removeAllItems();
        for (Movie m : bookingSystem.getMovies()) {
            cmbMovie.addItem(m.getMovieId() + " - " + m.getMovieName());
        }
        loadShowsForSelectedMovie();
    }

    private void clearForm() {
        txtCustomerName.setText("");
        txtPhone.setText("");
        txtEmail.setText("");
        txtSeat.setText("");
    }
}
