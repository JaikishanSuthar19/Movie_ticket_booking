package gui;

import model.Ticket;
import service.BookingSystem;

import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.util.LinkedList;

public class TicketPanel extends JPanel {

    private BookingSystem bookingSystem;

    private JTextField txtTicketId;
    private JTable ticketTable;
    private DefaultTableModel tableModel;

    public TicketPanel(BookingSystem bookingSystem) {
        this.bookingSystem = bookingSystem;
        setLayout(new BorderLayout(10, 10));
        setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        setBackground(new Color(245, 248, 255));

        add(createSearchPanel(), BorderLayout.NORTH);
        add(createTablePanel(), BorderLayout.CENTER);
        add(createButtonPanel(), BorderLayout.SOUTH);

        refreshTable();
    }

    private JPanel createSearchPanel() {
        JPanel panel = new JPanel(new FlowLayout(FlowLayout.LEFT, 10, 5));
        panel.setBackground(new Color(245, 248, 255));
        panel.setBorder(BorderFactory.createTitledBorder("Search Ticket"));

        txtTicketId = new JTextField(15);
        JButton btnSearch = new JButton("Search by Ticket ID");
        styleButton(btnSearch, new Color(23, 162, 184));
        btnSearch.addActionListener(e -> searchTicket());

        panel.add(new JLabel("Ticket ID:"));
        panel.add(txtTicketId);
        panel.add(btnSearch);

        return panel;
    }

    private JScrollPane createTablePanel() {
        String[] columns = {"Ticket ID", "Customer", "Movie", "Show Time", "Seat", "Price (Rs.)"};
        tableModel = new DefaultTableModel(columns, 0) {
            public boolean isCellEditable(int r, int c) { return false; }
        };
        ticketTable = new JTable(tableModel);
        ticketTable.setRowHeight(22);
        ticketTable.getTableHeader().setFont(new Font("Arial", Font.BOLD, 12));
        return new JScrollPane(ticketTable);
    }

    private JPanel createButtonPanel() {
        JPanel panel = new JPanel(new FlowLayout(FlowLayout.CENTER, 10, 5));
        panel.setBackground(new Color(245, 248, 255));

        JButton btnCancel = new JButton("Cancel Ticket");
        JButton btnViewBill = new JButton("View Bill");
        JButton btnRefresh = new JButton("Refresh All");

        styleButton(btnCancel, new Color(220, 53, 69));
        styleButton(btnViewBill, new Color(0, 123, 255));
        styleButton(btnRefresh, new Color(52, 58, 64));

        btnCancel.addActionListener(e -> cancelTicket());
        btnViewBill.addActionListener(e -> viewBill());
        btnRefresh.addActionListener(e -> refreshTable());

        panel.add(btnCancel);
        panel.add(btnViewBill);
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

    private void searchTicket() {
        String ticketId = txtTicketId.getText().trim();
        if (ticketId.isEmpty()) {
            JOptionPane.showMessageDialog(this, "Enter Ticket ID to search.", "Error", JOptionPane.ERROR_MESSAGE);
            return;
        }

        Ticket ticket = bookingSystem.searchTicket(ticketId);
        if (ticket == null) {
            JOptionPane.showMessageDialog(this, "Ticket not found: " + ticketId, "Not Found", JOptionPane.INFORMATION_MESSAGE);
            return;
        }

        tableModel.setRowCount(0);
        tableModel.addRow(new Object[]{
                ticket.getTicketId(),
                ticket.getCustomer().getName(),
                ticket.getMovie().getMovieName(),
                ticket.getShow().getShowTime(),
                ticket.getSeatNumber(),
                (int) ticket.getPrice()
        });
    }

    private void cancelTicket() {
        String ticketId = txtTicketId.getText().trim();
        if (ticketId.isEmpty()) {
            JOptionPane.showMessageDialog(this, "Enter Ticket ID to cancel.", "Error", JOptionPane.ERROR_MESSAGE);
            return;
        }

        Ticket ticket = bookingSystem.searchTicket(ticketId);
        if (ticket == null) {
            JOptionPane.showMessageDialog(this, "Ticket not found: " + ticketId, "Error", JOptionPane.ERROR_MESSAGE);
            return;
        }

        int confirm = JOptionPane.showConfirmDialog(this,
                "Cancel ticket " + ticketId + " for " + ticket.getCustomer().getName() + "?",
                "Confirm Cancellation",
                JOptionPane.YES_NO_OPTION);

        if (confirm == JOptionPane.YES_OPTION) {
            boolean cancelled = bookingSystem.cancelTicket(ticketId);
            if (cancelled) {
                refreshTable();
                txtTicketId.setText("");
                JOptionPane.showMessageDialog(this, "Ticket cancelled successfully.\nSeat " + ticket.getSeatNumber() + " is now available.", "Cancelled", JOptionPane.INFORMATION_MESSAGE);
            }
        }
    }

    private void viewBill() {
        String ticketId = txtTicketId.getText().trim();
        if (ticketId.isEmpty()) {
            JOptionPane.showMessageDialog(this, "Enter Ticket ID to view bill.", "Error", JOptionPane.ERROR_MESSAGE);
            return;
        }

        Ticket ticket = bookingSystem.searchTicket(ticketId);
        if (ticket == null) {
            JOptionPane.showMessageDialog(this, "Ticket not found: " + ticketId, "Error", JOptionPane.ERROR_MESSAGE);
            return;
        }

        JOptionPane.showMessageDialog(this, ticket.getBillInfo(), "Ticket Bill", JOptionPane.INFORMATION_MESSAGE);
    }

    public void refreshTable() {
        tableModel.setRowCount(0);
        // Iterate over LinkedList (booking order)
        LinkedList<Ticket> bookingList = bookingSystem.getBookingList();
        for (Ticket t : bookingList) {
            tableModel.addRow(new Object[]{
                    t.getTicketId(),
                    t.getCustomer().getName(),
                    t.getMovie().getMovieName(),
                    t.getShow().getShowTime(),
                    t.getSeatNumber(),
                    (int) t.getPrice()
            });
        }
    }
}
