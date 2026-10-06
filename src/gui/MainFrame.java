package gui;

import service.BookingSystem;

import javax.swing.*;
import java.awt.*;

public class MainFrame extends JFrame {

    private BookingSystem bookingSystem;
    private MoviePanel moviePanel;
    private BookingPanel bookingPanel;
    private TicketPanel ticketPanel;

    public MainFrame() {
        bookingSystem = new BookingSystem();

        setTitle("Movie Ticket Booking System");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(900, 600);
        setLocationRelativeTo(null); // center on screen
        setLayout(new BorderLayout());

        // Header
        JLabel header = new JLabel("  Movie Ticket Booking System", JLabel.LEFT);
        header.setFont(new Font("Arial", Font.BOLD, 20));
        header.setOpaque(true);
        header.setBackground(new Color(30, 60, 114));
        header.setForeground(Color.WHITE);
        header.setPreferredSize(new Dimension(900, 50));
        add(header, BorderLayout.NORTH);

        // Tabbed pane with 3 sections
        JTabbedPane tabbedPane = new JTabbedPane();
        tabbedPane.setFont(new Font("Arial", Font.BOLD, 13));

        moviePanel = new MoviePanel(bookingSystem);
        bookingPanel = new BookingPanel(bookingSystem);
        ticketPanel = new TicketPanel(bookingSystem);

        tabbedPane.addTab("  Movies  ", moviePanel);
        tabbedPane.addTab("  Book Ticket  ", bookingPanel);
        tabbedPane.addTab("  My Tickets  ", ticketPanel);

        // Refresh related panels when switching tabs
        tabbedPane.addChangeListener(e -> {
            int selected = tabbedPane.getSelectedIndex();
            if (selected == 0) moviePanel.refreshTable();
            if (selected == 1) bookingPanel.refreshMovies();
            if (selected == 2) ticketPanel.refreshTable();
        });

        add(tabbedPane, BorderLayout.CENTER);

        // Footer with Exit button
        JPanel footer = new JPanel(new FlowLayout(FlowLayout.RIGHT));
        footer.setBackground(new Color(30, 60, 114));
        JButton btnExit = new JButton("Exit");
        btnExit.setBackground(new Color(220, 53, 69));
        btnExit.setForeground(Color.WHITE);
        btnExit.setFont(new Font("Arial", Font.BOLD, 13));
        btnExit.setFocusPainted(false);
        btnExit.setOpaque(true);
        btnExit.setBorderPainted(false);
        btnExit.addActionListener(e -> {
            int confirm = JOptionPane.showConfirmDialog(this, "Exit application?", "Confirm Exit", JOptionPane.YES_NO_OPTION);
            if (confirm == JOptionPane.YES_OPTION) System.exit(0);
        });
        footer.add(btnExit);
        add(footer, BorderLayout.SOUTH);

        setVisible(true);
    }
}
