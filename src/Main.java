import gui.MainFrame;

import javax.swing.SwingUtilities;

public class Main {
    public static void main(String[] args) {
        // Run GUI on the Event Dispatch Thread (Swing best practice)
        SwingUtilities.invokeLater(() -> {
            new MainFrame();
        });
    }
}
