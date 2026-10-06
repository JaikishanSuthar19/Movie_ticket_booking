package gui;

import model.Movie;
import service.BookingSystem;

import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.util.ArrayList;

public class MoviePanel extends JPanel {

    private BookingSystem bookingSystem;

    private JTextField txtMovieName, txtGenre, txtDuration, txtRating, txtSearchId;
    private JTable movieTable;
    private DefaultTableModel tableModel;

    public MoviePanel(BookingSystem bookingSystem) {
        this.bookingSystem = bookingSystem;
        setLayout(new BorderLayout(10, 10));
        setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        setBackground(new Color(245, 248, 255));

        add(createFormPanel(), BorderLayout.NORTH);
        add(createTablePanel(), BorderLayout.CENTER);
        add(createButtonPanel(), BorderLayout.SOUTH);

        refreshTable();
    }

    private JPanel createFormPanel() {
        JPanel panel = new JPanel(new GridLayout(3, 4, 8, 8));
        panel.setBackground(new Color(245, 248, 255));
        panel.setBorder(BorderFactory.createTitledBorder("Movie Details"));

        txtMovieName = new JTextField();
        txtGenre     = new JTextField();
        txtDuration  = new JTextField();
        txtRating    = new JTextField();
        txtSearchId  = new JTextField();

        panel.add(new JLabel("Movie Name:"));
        panel.add(txtMovieName);
        panel.add(new JLabel("Genre:"));
        panel.add(txtGenre);
        panel.add(new JLabel("Duration (min):"));
        panel.add(txtDuration);
        panel.add(new JLabel("Rating (0-10):"));
        panel.add(txtRating);
        panel.add(new JLabel("Movie ID (for update/delete):"));
        panel.add(txtSearchId);
        panel.add(new JLabel(""));
        panel.add(new JLabel(""));

        return panel;
    }

    private JScrollPane createTablePanel() {
        String[] columns = {"Movie ID", "Movie Name", "Genre", "Duration (min)", "Rating"};
        tableModel = new DefaultTableModel(columns, 0) {
            public boolean isCellEditable(int r, int c) { return false; }
        };
        movieTable = new JTable(tableModel);
        movieTable.setRowHeight(22);
        movieTable.getTableHeader().setFont(new Font("Arial", Font.BOLD, 12));

        // Click a row → fill the search ID field automatically
        movieTable.getSelectionModel().addListSelectionListener(e -> {
            int row = movieTable.getSelectedRow();
            if (row >= 0) {
                txtSearchId.setText((String) tableModel.getValueAt(row, 0));
            }
        });

        return new JScrollPane(movieTable);
    }

    private JPanel createButtonPanel() {
        JPanel panel = new JPanel(new FlowLayout(FlowLayout.CENTER, 8, 5));
        panel.setBackground(new Color(245, 248, 255));

        JButton btnAdd       = new JButton("Add Movie");
        JButton btnUpdate    = new JButton("Update Movie");
        JButton btnDelete    = new JButton("Delete Movie");
        JButton btnSearch    = new JButton("Search Movie");
        JButton btnAddShow   = new JButton("Add Show for Movie");
        JButton btnSortName  = new JButton("Sort by Name");
        JButton btnSortRating = new JButton("Sort by Rating");
        JButton btnRefresh   = new JButton("Refresh");

        styleButton(btnAdd,        new Color(40, 167, 69));
        styleButton(btnUpdate,     new Color(0, 123, 255));
        styleButton(btnDelete,     new Color(220, 53, 69));
        styleButton(btnSearch,     new Color(23, 162, 184));
        styleButton(btnAddShow,    new Color(255, 140, 0));
        styleButton(btnSortName,   new Color(108, 117, 125));
        styleButton(btnSortRating, new Color(108, 117, 125));
        styleButton(btnRefresh,    new Color(52, 58, 64));

        btnAdd.addActionListener(e -> addMovie());
        btnUpdate.addActionListener(e -> updateMovie());
        btnDelete.addActionListener(e -> deleteMovie());
        btnSearch.addActionListener(e -> searchMovie());
        btnAddShow.addActionListener(e -> addShowForMovie());
        btnSortName.addActionListener(e -> sortByName());
        btnSortRating.addActionListener(e -> sortByRating());
        btnRefresh.addActionListener(e -> refreshTable());

        panel.add(btnAdd);
        panel.add(btnUpdate);
        panel.add(btnDelete);
        panel.add(btnSearch);
        panel.add(btnAddShow);
        panel.add(btnSortName);
        panel.add(btnSortRating);
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
        btn.setPreferredSize(new Dimension(150, 32));
    }

    private void addMovie() {
        try {
            String name     = txtMovieName.getText().trim();
            String genre    = txtGenre.getText().trim();
            String durStr   = txtDuration.getText().trim();
            String ratingStr = txtRating.getText().trim();

            if (name.isEmpty())   throw new Exception("Movie name cannot be empty.");
            if (genre.isEmpty())  throw new Exception("Genre cannot be empty.");
            if (durStr.isEmpty()) throw new Exception("Duration cannot be empty.");
            if (ratingStr.isEmpty()) throw new Exception("Rating cannot be empty.");

            int duration = Integer.parseInt(durStr);
            double rating = Double.parseDouble(ratingStr);

            if (rating < 0 || rating > 10) throw new Exception("Rating must be between 0 and 10.");

            bookingSystem.addMovie(name, genre, duration, rating);
            refreshTable();
            clearForm();
            JOptionPane.showMessageDialog(this,
                    "Movie added successfully!\nTip: Select the movie in the table and click 'Add Show for Movie' to add show times.",
                    "Success", JOptionPane.INFORMATION_MESSAGE);
        } catch (NumberFormatException e) {
            JOptionPane.showMessageDialog(this, "Duration and Rating must be valid numbers.", "Error", JOptionPane.ERROR_MESSAGE);
        } catch (Exception e) {
            JOptionPane.showMessageDialog(this, e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    // Add a show time for a movie — user enters Movie ID + show time
    private void addShowForMovie() {
        String movieId = txtSearchId.getText().trim();
        if (movieId.isEmpty()) {
            JOptionPane.showMessageDialog(this,
                    "Select a movie from the table first (or type the Movie ID in the ID field).",
                    "Select Movie", JOptionPane.WARNING_MESSAGE);
            return;
        }

        if (bookingSystem.searchMovie(movieId) == null) {
            JOptionPane.showMessageDialog(this, "Movie ID not found: " + movieId, "Error", JOptionPane.ERROR_MESSAGE);
            return;
        }

        String showTime = JOptionPane.showInputDialog(this,
                "Enter show time for Movie " + movieId + "\n(e.g.  10:00 AM  /  02:30 PM  /  07:00 PM)",
                "Add Show Time", JOptionPane.PLAIN_MESSAGE);

        if (showTime == null || showTime.trim().isEmpty()) return;

        bookingSystem.addShow(movieId, showTime.trim());
        JOptionPane.showMessageDialog(this,
                "Show added: " + showTime.trim() + " for movie " + movieId + "\nYou can now book tickets from the 'Book Ticket' tab.",
                "Show Added", JOptionPane.INFORMATION_MESSAGE);
    }

    private void updateMovie() {
        try {
            String id       = txtSearchId.getText().trim();
            String name     = txtMovieName.getText().trim();
            String genre    = txtGenre.getText().trim();
            String durStr   = txtDuration.getText().trim();
            String ratingStr = txtRating.getText().trim();

            if (id.isEmpty())   throw new Exception("Enter Movie ID to update.");
            if (name.isEmpty()) throw new Exception("Movie name cannot be empty.");

            int duration = Integer.parseInt(durStr);
            double rating = Double.parseDouble(ratingStr);

            boolean updated = bookingSystem.updateMovie(id, name, genre, duration, rating);
            if (updated) {
                refreshTable();
                clearForm();
                JOptionPane.showMessageDialog(this, "Movie updated successfully!", "Success", JOptionPane.INFORMATION_MESSAGE);
            } else {
                JOptionPane.showMessageDialog(this, "Movie ID not found: " + id, "Error", JOptionPane.ERROR_MESSAGE);
            }
        } catch (NumberFormatException e) {
            JOptionPane.showMessageDialog(this, "Duration and Rating must be valid numbers.", "Error", JOptionPane.ERROR_MESSAGE);
        } catch (Exception e) {
            JOptionPane.showMessageDialog(this, e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void deleteMovie() {
        String id = txtSearchId.getText().trim();
        if (id.isEmpty()) {
            JOptionPane.showMessageDialog(this, "Enter Movie ID to delete.", "Error", JOptionPane.ERROR_MESSAGE);
            return;
        }
        int confirm = JOptionPane.showConfirmDialog(this, "Delete movie " + id + "?", "Confirm", JOptionPane.YES_NO_OPTION);
        if (confirm == JOptionPane.YES_OPTION) {
            boolean deleted = bookingSystem.deleteMovie(id);
            if (deleted) {
                refreshTable();
                clearForm();
                JOptionPane.showMessageDialog(this, "Movie deleted.", "Success", JOptionPane.INFORMATION_MESSAGE);
            } else {
                JOptionPane.showMessageDialog(this, "Movie ID not found.", "Error", JOptionPane.ERROR_MESSAGE);
            }
        }
    }

    private void searchMovie() {
        String query = txtSearchId.getText().trim();
        if (query.isEmpty()) {
            JOptionPane.showMessageDialog(this, "Enter Movie ID or name to search.", "Error", JOptionPane.ERROR_MESSAGE);
            return;
        }

        tableModel.setRowCount(0);

        Movie m = bookingSystem.searchMovie(query);
        if (m != null) {
            tableModel.addRow(new Object[]{m.getMovieId(), m.getMovieName(), m.getGenre(), m.getDuration(), m.getRating()});
            return;
        }

        ArrayList<Movie> results = bookingSystem.searchMovieByName(query);
        if (results.isEmpty()) {
            JOptionPane.showMessageDialog(this, "No movies found for: " + query, "Not Found", JOptionPane.INFORMATION_MESSAGE);
            refreshTable();
        } else {
            for (Movie movie : results) {
                tableModel.addRow(new Object[]{movie.getMovieId(), movie.getMovieName(), movie.getGenre(), movie.getDuration(), movie.getRating()});
            }
        }
    }

    private void sortByName() {
        ArrayList<Movie> sorted = bookingSystem.getMoviesSortedByName();
        tableModel.setRowCount(0);
        for (Movie m : sorted) {
            tableModel.addRow(new Object[]{m.getMovieId(), m.getMovieName(), m.getGenre(), m.getDuration(), m.getRating()});
        }
    }

    private void sortByRating() {
        ArrayList<Movie> sorted = bookingSystem.getMoviesSortedByRating();
        tableModel.setRowCount(0);
        for (Movie m : sorted) {
            tableModel.addRow(new Object[]{m.getMovieId(), m.getMovieName(), m.getGenre(), m.getDuration(), m.getRating()});
        }
    }

    public void refreshTable() {
        tableModel.setRowCount(0);
        for (Movie m : bookingSystem.getMovies()) {
            tableModel.addRow(new Object[]{m.getMovieId(), m.getMovieName(), m.getGenre(), m.getDuration(), m.getRating()});
        }
    }

    private void clearForm() {
        txtMovieName.setText("");
        txtGenre.setText("");
        txtDuration.setText("");
        txtRating.setText("");
        txtSearchId.setText("");
    }
}
