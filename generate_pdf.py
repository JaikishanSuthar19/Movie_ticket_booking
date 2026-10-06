"""
PDF Documentation Generator
Movie Ticket Booking System
Student: Jaikishan Suthar | Roll No: 150096752152
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, Image, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import Flowable
import os, glob

# ─── Output path ────────────────────────────────────────────────────────────
OUT = "/Users/jaikishansuthar/Desktop/movietickets/Movie_Ticket_Booking_System_Documentation.pdf"
IMG_DIR = "/Users/jaikishansuthar/Desktop/movietickets"

# ─── Find screenshots ───────────────────────────────────────────────────────
screenshots = sorted(glob.glob(os.path.join(IMG_DIR, "*.png")))

# ─── Colours ────────────────────────────────────────────────────────────────
DARK_BLUE   = colors.HexColor("#1E3C72")
MID_BLUE    = colors.HexColor("#2A5298")
LIGHT_BLUE  = colors.HexColor("#EBF2FF")
ACCENT      = colors.HexColor("#28A745")
RED         = colors.HexColor("#DC3545")
ORANGE      = colors.HexColor("#FF8C00")
HEADER_TEXT = colors.white
BODY_TEXT   = colors.HexColor("#222222")
GREY_ROW    = colors.HexColor("#F5F8FF")
BORDER      = colors.HexColor("#CCCCCC")

# ─── Styles ─────────────────────────────────────────────────────────────────
base_styles = getSampleStyleSheet()

def sty(name, parent="Normal", **kw):
    s = ParagraphStyle(name, parent=base_styles[parent], **kw)
    return s

S = {
    "cover_title": sty("cover_title", fontSize=28, textColor=HEADER_TEXT,
                        alignment=TA_CENTER, fontName="Helvetica-Bold", spaceAfter=8),
    "cover_sub":   sty("cover_sub",   fontSize=14, textColor=HEADER_TEXT,
                        alignment=TA_CENTER, fontName="Helvetica", spaceAfter=6),
    "cover_small": sty("cover_small", fontSize=11, textColor=colors.HexColor("#CCDDFF"),
                        alignment=TA_CENTER, fontName="Helvetica"),
    "h1":  sty("h1",  fontSize=15, textColor=HEADER_TEXT, fontName="Helvetica-Bold",
                alignment=TA_LEFT, spaceAfter=4, spaceBefore=6),
    "h2":  sty("h2",  fontSize=12, textColor=DARK_BLUE,   fontName="Helvetica-Bold",
                spaceAfter=3, spaceBefore=8),
    "body": sty("body", fontSize=9.5, textColor=BODY_TEXT, leading=14,
                 spaceAfter=4, alignment=TA_JUSTIFY),
    "bullet": sty("bullet", fontSize=9.5, textColor=BODY_TEXT, leading=13,
                   leftIndent=14, spaceAfter=2),
    "code": sty("code", fontSize=8.5, fontName="Courier", textColor=DARK_BLUE,
                 backColor=LIGHT_BLUE, leading=12, leftIndent=10, spaceAfter=4),
    "caption": sty("caption", fontSize=8, textColor=colors.HexColor("#555555"),
                    alignment=TA_CENTER, spaceBefore=2, spaceAfter=8),
    "toc_entry": sty("toc_entry", fontSize=10, textColor=DARK_BLUE, leading=18,
                      leftIndent=10),
    "flow_step": sty("flow_step", fontSize=9.5, textColor=DARK_BLUE,
                      fontName="Helvetica-Bold", alignment=TA_CENTER),
}

# ─── Helper: section heading bar ────────────────────────────────────────────
class SectionHeader(Flowable):
    def __init__(self, text, width=None, bgcolor=DARK_BLUE, height=24):
        super().__init__()
        self.text   = text
        self.width  = width or (A4[0] - 2.8*cm)
        self.bgcolor = bgcolor
        self.height  = height
    def wrap(self, aw, ah):
        return self.width, self.height + 6
    def draw(self):
        c = self.canv
        c.setFillColor(self.bgcolor)
        c.roundRect(0, 2, self.width, self.height, 4, fill=1, stroke=0)
        c.setFillColor(HEADER_TEXT)
        c.setFont("Helvetica-Bold", 11)
        c.drawString(10, 8, self.text)

# ─── Helper: coloured table ──────────────────────────────────────────────────
def make_table(headers, rows, col_widths=None):
    data = [headers] + rows
    t = Table(data, colWidths=col_widths, repeatRows=1)
    n = len(rows)
    style = [
        ("BACKGROUND",   (0,0), (-1,0), DARK_BLUE),
        ("TEXTCOLOR",    (0,0), (-1,0), colors.white),
        ("FONTNAME",     (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE",     (0,0), (-1,0), 9),
        ("ALIGN",        (0,0), (-1,-1), "LEFT"),
        ("VALIGN",       (0,0), (-1,-1), "MIDDLE"),
        ("FONTSIZE",     (0,1), (-1,-1), 8.5),
        ("FONTNAME",     (0,1), (-1,-1), "Helvetica"),
        ("TEXTCOLOR",    (0,1), (-1,-1), BODY_TEXT),
        ("ROWBACKGROUNDS",(0,1),(-1,-1), [GREY_ROW, colors.white]),
        ("GRID",         (0,0), (-1,-1), 0.4, BORDER),
        ("TOPPADDING",   (0,0), (-1,-1), 4),
        ("BOTTOMPADDING",(0,0), (-1,-1), 4),
        ("LEFTPADDING",  (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ]
    t.setStyle(TableStyle(style))
    return t

def P(text, style="body"):
    return Paragraph(text, S[style])

def B(text):
    return Paragraph(f"• {text}", S["bullet"])

def H(text, color=DARK_BLUE):
    return SectionHeader(text, bgcolor=color)

def sp(h=6):
    return Spacer(1, h)

def hr():
    return HRFlowable(width="100%", thickness=0.5, color=BORDER, spaceAfter=4)

# ─── Image helper ────────────────────────────────────────────────────────────
def add_image(path, caption, max_w=14*cm, max_h=8*cm):
    elems = []
    if path and os.path.exists(path):
        try:
            img = Image(path)
            w, h = img.imageWidth, img.imageHeight
            ratio = min(max_w/w, max_h/h)
            img.drawWidth  = w * ratio
            img.drawHeight = h * ratio
            # centre it
            tbl = Table([[img]], colWidths=[A4[0]-2.8*cm])
            tbl.setStyle(TableStyle([
                ("ALIGN",  (0,0), (-1,-1), "CENTER"),
                ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                ("BOX",    (0,0), (-1,-1), 0.5, BORDER),
                ("BACKGROUND", (0,0), (-1,-1), colors.white),
            ]))
            elems.append(tbl)
            elems.append(P(f"<i>{caption}</i>", "caption"))
        except Exception as e:
            elems.append(P(f"[Screenshot: {caption}]", "caption"))
    return elems

# ─── Page template ───────────────────────────────────────────────────────────
def on_page(canvas, doc):
    canvas.saveState()
    w, h = A4
    # header strip
    canvas.setFillColor(DARK_BLUE)
    canvas.rect(0, h-1.1*cm, w, 1.1*cm, fill=1, stroke=0)
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica-Bold", 8)
    canvas.drawString(1*cm, h-0.75*cm, "Movie Ticket Booking System")
    canvas.setFont("Helvetica", 8)
    canvas.drawRightString(w-1*cm, h-0.75*cm, "Jaikishan Suthar | 150096752152")
    # footer strip
    canvas.setFillColor(DARK_BLUE)
    canvas.rect(0, 0, w, 0.7*cm, fill=1, stroke=0)
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica", 8)
    canvas.drawString(1*cm, 0.22*cm, "B.Tech CSE — Java Programming Case Study")
    canvas.drawRightString(w-1*cm, 0.22*cm, f"Page {doc.page}")
    canvas.restoreState()

def on_cover(canvas, doc):
    canvas.saveState()
    w, h = A4
    # full blue cover gradient simulation
    canvas.setFillColor(DARK_BLUE)
    canvas.rect(0, 0, w, h, fill=1, stroke=0)
    # diagonal accent stripe
    canvas.setFillColor(MID_BLUE)
    from reportlab.graphics.shapes import Drawing
    p = canvas.beginPath()
    p.moveTo(0, h*0.35)
    p.lineTo(w, h*0.15)
    p.lineTo(w, 0)
    p.lineTo(0, 0)
    p.close()
    canvas.drawPath(p, fill=1, stroke=0)
    canvas.restoreState()

# ─── Build story ─────────────────────────────────────────────────────────────
story = []

# ══════════════════════════════════════════════════════
# COVER PAGE
# ══════════════════════════════════════════════════════
story.append(Spacer(1, 3.5*cm))
story.append(Paragraph("🎬 Movie Ticket Booking System", S["cover_title"]))
story.append(Spacer(1, 0.4*cm))
story.append(HRFlowable(width="60%", thickness=1.5, color=colors.HexColor("#4A90D9"),
                          hAlign="CENTER", spaceAfter=12))
story.append(Paragraph("B.Tech CSE — Java Programming Case Study", S["cover_sub"]))
story.append(Spacer(1, 1.2*cm))

cover_info = Table([
    ["Student Name",  "Jaikishan Suthar"],
    ["Roll Number",   "150096752152"],
    ["Subject",       "Java Programming Lab"],
    ["Technology",    "Java 17+  |  Java Swing  |  Collections Framework"],
    ["Project Type",  "Desktop Application"],
], colWidths=[5.5*cm, 9*cm])
cover_info.setStyle(TableStyle([
    ("BACKGROUND",  (0,0), (0,-1), MID_BLUE),
    ("TEXTCOLOR",   (0,0), (0,-1), colors.white),
    ("FONTNAME",    (0,0), (0,-1), "Helvetica-Bold"),
    ("BACKGROUND",  (1,0), (1,-1), colors.HexColor("#1A3460")),
    ("TEXTCOLOR",   (1,0), (1,-1), colors.HexColor("#CCDCFF")),
    ("FONTNAME",    (1,0), (1,-1), "Helvetica"),
    ("FONTSIZE",    (0,0), (-1,-1), 10),
    ("TOPPADDING",  (0,0), (-1,-1), 8),
    ("BOTTOMPADDING",(0,0),(-1,-1), 8),
    ("LEFTPADDING", (0,0), (-1,-1), 12),
    ("GRID",        (0,0), (-1,-1), 0.3, colors.HexColor("#2A4A8A")),
    ("ALIGN",       (0,0), (-1,-1), "LEFT"),
]))
story.append(cover_info)
story.append(Spacer(1, 2*cm))
story.append(Paragraph("Submitted as part of Java Programming Course", S["cover_small"]))
story.append(PageBreak())

# ══════════════════════════════════════════════════════
# TABLE OF CONTENTS
# ══════════════════════════════════════════════════════
story.append(H("TABLE OF CONTENTS"))
story.append(sp(8))
toc_data = [
    ("1.", "Introduction"),
    ("2.", "Objectives"),
    ("3.", "Technologies Used"),
    ("4.", "Project Features"),
    ("5.", "Project Structure"),
    ("6.", "Java Concepts Used"),
    ("7.", "OOP Concepts"),
    ("8.", "GUI Components"),
    ("9.", "Java File Explanation"),
    ("10.", "Project Working Flow"),
    ("11.", "Screenshots"),
    ("12.", "Testing"),
    ("13.", "Conclusion"),
]
for no, title in toc_data:
    row = Table([[P(f"<b>{no}</b>", "body"), P(title, "body"),
                  P("· · · · · · · · · · · · · · · · · · ·", "body")]],
                colWidths=[1*cm, 8*cm, 6.5*cm])
    row.setStyle(TableStyle([
        ("VALIGN",  (0,0), (-1,-1), "MIDDLE"),
        ("ALIGN",   (2,0), (2,0),   "RIGHT"),
        ("LINEBELOW",(0,0),(-1,0), 0.3, colors.HexColor("#DDDDDD")),
        ("TOPPADDING",(0,0),(-1,-1),3),
        ("BOTTOMPADDING",(0,0),(-1,-1),3),
    ]))
    story.append(row)

story.append(PageBreak())

# ══════════════════════════════════════════════════════
# SECTION 1 — INTRODUCTION
# ══════════════════════════════════════════════════════
story.append(H("1.  INTRODUCTION"))
story.append(sp(8))
story.append(P("The <b>Movie Ticket Booking System</b> is a desktop application developed in Java as part of the B.Tech CSE Java Programming course. It allows a user to manage movies, book seats for shows, generate tickets, and cancel bookings — all through a simple graphical interface built with Java Swing."))
story.append(sp(4))
story.append(P("This project demonstrates core Java programming concepts including Object-Oriented Programming (OOP), Java Collections Framework, Exception Handling, Validation, and GUI development — making it a complete and practical case study."))
story.append(sp(6))

intro_table = make_table(
    ["Aspect", "Details"],
    [
        ["What I Made",    "A Java Swing desktop application for booking movie tickets"],
        ["Problem Solved", "Manual ticket booking is slow and error-prone; this automates the process"],
        ["Who Uses It",    "Cinema staff or customers at a booking counter"],
        ["Why Useful",     "Prevents duplicate seat booking, tracks all tickets, generates bills instantly"],
        ["Data Storage",   "In-memory using Java Collections (no database needed)"],
    ],
    col_widths=[4.5*cm, 11*cm]
)
story.append(intro_table)

# ══════════════════════════════════════════════════════
# SECTION 2 — OBJECTIVES
# ══════════════════════════════════════════════════════
story.append(sp(10))
story.append(H("2.  OBJECTIVES"))
story.append(sp(8))
objectives = [
    "Develop a complete Movie Ticket Booking System using Java Swing.",
    "Implement all required Java Collections: Array, ArrayList, LinkedList, HashMap, TreeMap.",
    "Demonstrate OOP concepts: Classes, Objects, Encapsulation, Inheritance, Constructors.",
    "Provide a graphical user interface with three main modules: Movies, Book Ticket, My Tickets.",
    "Implement CRUD operations for Movie management (Create, Read, Update, Delete).",
    "Implement seat booking with duplicate-booking prevention.",
    "Generate formatted ticket bills using JOptionPane.",
    "Apply exception handling and input validation throughout the application.",
    "Keep the project simple, readable, and suitable for a college submission.",
]
for obj in objectives:
    story.append(B(obj))

# ══════════════════════════════════════════════════════
# SECTION 3 — TECHNOLOGIES USED
# ══════════════════════════════════════════════════════
story.append(sp(10))
story.append(H("3.  TECHNOLOGIES USED"))
story.append(sp(8))
story.append(make_table(
    ["Technology / Tool", "Version", "Purpose"],
    [
        ["Java",                  "17+",          "Core programming language"],
        ["Java Swing",            "Built-in",     "GUI framework for desktop application"],
        ["Java Collections",      "Built-in",     "ArrayList, LinkedList, HashMap, TreeMap"],
        ["Java AWT",              "Built-in",     "Layout managers, Colors, Fonts"],
        ["IntelliJ IDEA / Kiro",  "Any",          "IDE used to write and run the project"],
        ["JDK",                   "17+",          "Java Development Kit for compiling and running"],
        ["No External Libraries", "—",            "Only standard Java libraries used"],
    ],
    col_widths=[5.5*cm, 2.5*cm, 7.5*cm]
))

story.append(PageBreak())

# ══════════════════════════════════════════════════════
# SECTION 4 — PROJECT FEATURES
# ══════════════════════════════════════════════════════
story.append(H("4.  PROJECT FEATURES"))
story.append(sp(8))
story.append(make_table(
    ["Feature", "What Happens", "Tab"],
    [
        ["Add Movie",         "Enter name, genre, duration, rating → stored in ArrayList",      "Movies"],
        ["Update Movie",      "Select movie ID → edit fields → update in ArrayList",            "Movies"],
        ["Delete Movie",      "Select movie ID → confirm → removed from ArrayList",             "Movies"],
        ["Search Movie",      "Search by ID or name → result shown in table",                   "Movies"],
        ["Sort Movies",       "Sort by Name (A-Z) or Rating (highest first)",                   "Movies"],
        ["Add Show",          "Select movie → enter time → show added to TreeMap",              "Movies"],
        ["View Seats",        "Select show → seat map shown (free / [booked])",                 "Book Ticket"],
        ["Book Ticket",       "Enter customer details + seat → ticket created → bill shown",    "Book Ticket"],
        ["Prevent Duplicate", "Same seat cannot be booked twice — shows error popup",           "Book Ticket"],
        ["Search Ticket",     "Enter Ticket ID → ticket details shown in table",                "My Tickets"],
        ["Cancel Ticket",     "Enter Ticket ID → confirm → seat freed, ticket removed",         "My Tickets"],
        ["View Bill",         "Enter Ticket ID → formatted bill shown in popup",                "My Tickets"],
    ],
    col_widths=[4*cm, 8*cm, 3.5*cm]
))

# ══════════════════════════════════════════════════════
# SECTION 5 — PROJECT STRUCTURE
# ══════════════════════════════════════════════════════
story.append(sp(10))
story.append(H("5.  PROJECT STRUCTURE"))
story.append(sp(8))
story.append(Paragraph("""
<font name="Courier" size="9" color="#1E3C72">
MovieTicketBookingSystem/<br/>
├── src/<br/>
│   ├── model/<br/>
│   │   ├── Movie.java<br/>
│   │   ├── Show.java<br/>
│   │   ├── Customer.java<br/>
│   │   ├── Ticket.java<br/>
│   │   └── SeatAlreadyBookedException.java<br/>
│   ├── service/<br/>
│   │   └── BookingSystem.java<br/>
│   ├── gui/<br/>
│   │   ├── MainFrame.java<br/>
│   │   ├── MoviePanel.java<br/>
│   │   ├── BookingPanel.java<br/>
│   │   └── TicketPanel.java<br/>
│   └── Main.java<br/>
├── README.md<br/>
├── VIVA.md<br/>
└── CODE.md
</font>
""", S["body"]))
story.append(sp(4))
story.append(make_table(
    ["File", "Package", "Purpose"],
    [
        ["Main.java",                      "—",       "Entry point — starts the Swing application"],
        ["Movie.java",                     "model",   "Blueprint for a movie (ID, name, genre, duration, rating)"],
        ["Customer.java",                  "model",   "Blueprint for a customer (ID, name, phone, email) + validation"],
        ["Show.java",                      "model",   "Manages a show — movie, time, seat array, book/cancel logic"],
        ["Ticket.java",                    "model",   "Stores booking info — customer, movie, show, seat, price + bill"],
        ["SeatAlreadyBookedException.java","model",   "Custom exception for duplicate seat booking"],
        ["BookingSystem.java",             "service", "Core logic — all 5 collections + all CRUD/booking methods"],
        ["MainFrame.java",                 "gui",     "Main JFrame window — header, 3 tabs, exit button"],
        ["MoviePanel.java",                "gui",     "Movies tab — add/update/delete/search/sort movies and shows"],
        ["BookingPanel.java",              "gui",     "Book Ticket tab — select movie/show/seat, enter details, book"],
        ["TicketPanel.java",               "gui",     "My Tickets tab — search, cancel, view bill"],
    ],
    col_widths=[5.5*cm, 2.5*cm, 7.5*cm]
))

story.append(PageBreak())

# ══════════════════════════════════════════════════════
# SECTION 6 — JAVA CONCEPTS USED
# ══════════════════════════════════════════════════════
story.append(H("6.  JAVA CONCEPTS USED"))
story.append(sp(8))
story.append(make_table(
    ["Concept", "Meaning", "Where Used in Project"],
    [
        ["Class",             "Blueprint to create objects",                       "Movie, Customer, Show, Ticket, BookingSystem"],
        ["Object",            "Instance of a class",                               "new Movie(...), new Ticket(...), new BookingSystem()"],
        ["Constructor",       "Method called when object is created",              "All model classes — Movie(id, name, genre, ...)"],
        ["Array",             "Fixed-size collection of same type",                "Show.java — String[] seats, boolean[] seatBooked"],
        ["ArrayList",         "Dynamic list — grows/shrinks",                      "BookingSystem — ArrayList<Movie>, ArrayList<Customer>"],
        ["LinkedList",        "Ordered list — preserves insertion order",          "BookingSystem — LinkedList<Ticket> bookingList"],
        ["HashMap",           "Key-value pairs — fast lookup by key",              "BookingSystem — HashMap<String, Ticket> tickets"],
        ["TreeMap",           "Key-value pairs — automatically sorted by key",     "BookingSystem — TreeMap<String, Show> shows"],
        ["Methods",           "Named blocks of code that perform a task",          "addMovie(), bookTicket(), cancelTicket(), searchTicket()"],
        ["CRUD",              "Create, Read, Update, Delete operations",            "Movie: addMovie, getMovies, updateMovie, deleteMovie"],
        ["Searching",         "Finding data by a key/value",                       "searchMovie(ID), searchTicket(ID) via HashMap.get()"],
        ["Sorting",           "Arranging data in order",                           "getMoviesSortedByName(), getMoviesSortedByRating()"],
        ["Exception Handling","try-catch to handle runtime errors gracefully",     "bookTicket() — catches SeatAlreadyBookedException"],
        ["Validation",        "Checking input before processing",                  "Customer.isValidPhone(), isValidName(), empty checks"],
        ["Event Handling",    "Responding to button clicks/actions in GUI",        "btnBook.addActionListener(e -> bookTicket())"],
        ["Comparator",        "Defines custom sort order",                         "Comparator.comparing(Movie::getMovieName)"],
        ["Lambda Expression", "Short anonymous function",                          "(m1, m2) -> Double.compare(m2.getRating(), m1.getRating())"],
    ],
    col_widths=[3.5*cm, 5*cm, 7*cm]
))

# ══════════════════════════════════════════════════════
# SECTION 7 — OOP CONCEPTS
# ══════════════════════════════════════════════════════
story.append(sp(10))
story.append(H("7.  OOP CONCEPTS"))
story.append(sp(8))
story.append(make_table(
    ["OOP Concept", "Used?", "Example From My Project"],
    [
        ["Class",         "✅ Used",     "Movie, Customer, Show, Ticket — all are classes"],
        ["Object",        "✅ Used",     "new Movie(\"M001\", \"Avengers\", ...) creates an object"],
        ["Constructor",   "✅ Used",     "public Movie(String id, String name, ...) — in every model class"],
        ["Encapsulation", "✅ Used",     "private fields in Movie.java — accessed only via getters/setters"],
        ["Inheritance",   "✅ Used",     "SeatAlreadyBookedException extends Exception; MainFrame extends JFrame"],
        ["Polymorphism",  "✅ Used",     "@Override toString() in Movie, Customer, Show, Ticket"],
        ["Abstraction",   "Partial",     "BookingSystem hides data logic from GUI panels (design-level)"],
    ],
    col_widths=[4*cm, 2.5*cm, 9*cm]
))

story.append(PageBreak())

# ══════════════════════════════════════════════════════
# SECTION 8 — GUI COMPONENTS
# ══════════════════════════════════════════════════════
story.append(H("8.  GUI COMPONENTS (JAVA SWING)"))
story.append(sp(8))
story.append(make_table(
    ["Component", "What It Does", "Where Used"],
    [
        ["JFrame",          "Main application window",                           "MainFrame.java — the outer window"],
        ["JPanel",          "Container to group components",                     "MoviePanel, BookingPanel, TicketPanel"],
        ["JTabbedPane",     "Tabbed navigation between screens",                 "MainFrame.java — Movies / Book Ticket / My Tickets"],
        ["JLabel",          "Displays text (non-editable)",                      "Field labels: 'Movie Name:', 'Genre:', etc."],
        ["JTextField",      "Single-line text input box",                        "txtMovieName, txtPhone, txtSeat, etc."],
        ["JTextArea",       "Multi-line text display",                           "BookingPanel — shows seat layout"],
        ["JButton",         "Clickable button",                                  "Add Movie, Book Ticket, Cancel Ticket, Exit, etc."],
        ["JComboBox",       "Dropdown selector",                                 "BookingPanel — cmbMovie (movie list), cmbShow (show times)"],
        ["JTable",          "Displays data in rows and columns",                 "MoviePanel (movie list), TicketPanel (ticket list)"],
        ["DefaultTableModel","Data model for JTable",                            "MoviePanel and TicketPanel — stores cell data"],
        ["JScrollPane",     "Adds scrollbar to JTable or JTextArea",             "Wraps movieTable, ticketTable, txtAvailableSeats"],
        ["JOptionPane",     "Shows popup dialogs (info, error, confirm, input)", "Error messages, success confirmations, bill display"],
        ["BorderLayout",    "Layout: NORTH, SOUTH, EAST, WEST, CENTER",          "MainFrame, MoviePanel, BookingPanel, TicketPanel"],
        ["GridLayout",      "Grid of rows × columns",                            "Form panels in MoviePanel and BookingPanel"],
        ["FlowLayout",      "Left-to-right button row",                          "Button panels in all GUI files"],
        ["ActionListener",  "Interface for button click events",                 "All buttons — btnAdd, btnBook, btnCancel, etc."],
        ["ChangeListener",  "Fires when tab is switched",                        "MainFrame — refreshes panel data on tab change"],
    ],
    col_widths=[3.8*cm, 6*cm, 5.7*cm]
))

# ══════════════════════════════════════════════════════
# SECTION 9 — JAVA FILE EXPLANATION
# ══════════════════════════════════════════════════════
story.append(sp(10))
story.append(H("9.  JAVA FILE EXPLANATION"))
story.append(sp(8))

files_data = [
    ("Main.java", "Entry Point",
     "Starts the application. Calls SwingUtilities.invokeLater() to safely launch the GUI on the Event Dispatch Thread. Creates a new MainFrame object which opens the main window.",
     "SwingUtilities.invokeLater(() -> { new MainFrame(); });"),

    ("Movie.java", "Model — Movie Blueprint",
     "Defines the Movie class with 5 private fields: movieId, movieName, genre, duration, rating. Includes a constructor, getters, setters, and toString().",
     "private String movieId, movieName, genre;\nprivate int duration;\nprivate double rating;"),

    ("Customer.java", "Model — Customer Blueprint",
     "Defines the Customer class. Includes static validation methods isValidPhone() (checks 10 digits) and isValidName() (checks not empty).",
     'phone.matches("\\\\d{10}") → validates 10-digit phone number'),

    ("Show.java", "Model — Show with Seat Array",
     "Manages a cinema show. Uses two parallel Arrays: String[] seats (seat names A1-C5) and boolean[] seatBooked (true/false per seat). Methods: isSeatAvailable(), bookSeat(), cancelSeat(), getAllSeatsInfo().",
     "String[] seats = new String[15];\nboolean[] seatBooked = new boolean[15];"),

    ("Ticket.java", "Model — Ticket / Bill",
     "Stores complete booking info: customer, movie, show, seat, price. getBillInfo() returns a formatted bill string shown in the popup dialog.",
     '"Ticket ID : " + ticketId + "\\nCustomer : " + customer.getName()'),

    ("SeatAlreadyBookedException.java", "Custom Exception",
     "A custom exception class that extends Exception. Thrown specifically when a user tries to book an already-booked seat, allowing the GUI to show a special warning message.",
     "public class SeatAlreadyBookedException extends Exception { ... }"),

    ("BookingSystem.java", "Service — Core Logic",
     "The brain of the application. Declares all 5 Java Collections. Implements all business logic: addMovie, updateMovie, deleteMovie, addShow, bookTicket, cancelTicket, searchTicket. All GUI panels use this class.",
     "ArrayList<Movie> movies;  LinkedList<Ticket> bookingList;\nHashMap<String, Ticket> tickets;  TreeMap<String, Show> shows;"),

    ("MainFrame.java", "GUI — Main Window",
     "Extends JFrame. Creates the main window (900×600), blue header, JTabbedPane with 3 tabs, and an Exit button. Shares one BookingSystem instance with all 3 panels.",
     "public class MainFrame extends JFrame { ... }"),

    ("MoviePanel.java", "GUI — Movies Tab",
     "Extends JPanel. Provides form fields and 8 buttons for movie management. Clicking a table row auto-fills the Movie ID. The 'Add Show for Movie' button lets users add show times for any movie.",
     "movieTable.getSelectionModel().addListSelectionListener(...)"),

    ("BookingPanel.java", "GUI — Book Ticket Tab",
     "Extends JPanel. Left side: booking form with dropdowns for movie and show. Right side: seat map. When movie changes, shows auto-load. Book Ticket button calls bookingSystem.bookTicket() and shows the bill.",
     "cmbMovie.addActionListener(e -> loadShowsForSelectedMovie());"),

    ("TicketPanel.java", "GUI — My Tickets Tab",
     "Extends JPanel. Shows all booked tickets in a table (from LinkedList). Supports search by Ticket ID (using HashMap), cancel ticket, and view bill.",
     "LinkedList<Ticket> bookingList = bookingSystem.getBookingList();"),
]

for fname, role, desc, code_snippet in files_data:
    story.append(KeepTogether([
        Table([[
            Paragraph(f"<b>{fname}</b>", S["body"]),
            Paragraph(f"<i>{role}</i>", S["body"]),
        ]], colWidths=[5.5*cm, 10*cm], style=TableStyle([
            ("BACKGROUND", (0,0), (0,0), LIGHT_BLUE),
            ("BACKGROUND", (1,0), (1,0), colors.white),
            ("GRID",       (0,0), (-1,-1), 0.4, BORDER),
            ("FONTNAME",   (0,0), (0,0), "Helvetica-Bold"),
            ("LEFTPADDING",(0,0),(-1,-1), 6),
            ("TOPPADDING", (0,0),(-1,-1), 4),
            ("BOTTOMPADDING",(0,0),(-1,-1), 4),
        ])),
        Spacer(1, 2),
        Paragraph(desc, S["body"]),
        Paragraph(f'<font name="Courier" size="8" color="#1E3C72">{code_snippet}</font>', S["body"]),
        Spacer(1, 6),
    ]))

story.append(PageBreak())

# ══════════════════════════════════════════════════════
# SECTION 10 — PROJECT WORKING FLOW
# ══════════════════════════════════════════════════════
story.append(H("10.  PROJECT WORKING FLOW"))
story.append(sp(8))

flow_steps = [
    ("Main.java",         "Application starts here",                              DARK_BLUE),
    ("MainFrame.java",    "Creates window, tabs, shared BookingSystem",            MID_BLUE),
    ("BookingSystem.java","Loads 4 sample movies + 4 sample shows",               DARK_BLUE),
    ("MoviePanel",        "User adds/updates/deletes/searches movies and shows",   MID_BLUE),
    ("BookingPanel",      "User selects movie → show → sees seat map",            DARK_BLUE),
    ("BookingPanel",      "User enters name, phone, seat → clicks Book Ticket",    MID_BLUE),
    ("BookingSystem",     "Validates → registers customer → books seat → creates ticket", DARK_BLUE),
    ("HashMap + LinkedList","Ticket stored in both collections",                   MID_BLUE),
    ("JOptionPane",       "Bill popup: Ticket ID, Customer, Movie, Seat, Price",   ACCENT),
    ("TicketPanel",       "All tickets shown from LinkedList in table",            DARK_BLUE),
    ("TicketPanel",       "Search by ID (HashMap.get) → view bill or cancel",      MID_BLUE),
    ("cancelTicket()",    "Seat freed in Show → removed from HashMap + LinkedList", RED),
]

for step, desc, col in flow_steps:
    row = Table([
        [Paragraph(f"<b>{step}</b>", S["flow_step"]),
         Paragraph(desc, S["body"])],
    ], colWidths=[4.5*cm, 11*cm])
    row.setStyle(TableStyle([
        ("BACKGROUND",  (0,0), (0,0), col),
        ("TEXTCOLOR",   (0,0), (0,0), colors.white),
        ("BACKGROUND",  (1,0), (1,0), colors.white),
        ("GRID",        (0,0), (-1,-1), 0.4, BORDER),
        ("ALIGN",       (0,0), (0,0), "CENTER"),
        ("VALIGN",      (0,0), (-1,-1), "MIDDLE"),
        ("LEFTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING",  (0,0), (-1,-1), 5),
        ("BOTTOMPADDING",(0,0),(-1,-1), 5),
    ]))
    story.append(row)
    # arrow
    arr = Table([["▼"]], colWidths=[A4[0]-2.8*cm])
    arr.setStyle(TableStyle([
        ("ALIGN",   (0,0), (-1,-1), "LEFT"),
        ("FONTSIZE",(0,0), (-1,-1), 8),
        ("TEXTCOLOR",(0,0),(-1,-1), colors.HexColor("#888888")),
        ("LEFTPADDING",(0,0),(-1,-1), 30),
        ("TOPPADDING",(0,0),(-1,-1), 0),
        ("BOTTOMPADDING",(0,0),(-1,-1), 0),
    ]))
    story.append(arr)

story.append(PageBreak())

# ══════════════════════════════════════════════════════
# SECTION 11 — SCREENSHOTS
# ══════════════════════════════════════════════════════
story.append(H("11.  SCREENSHOTS"))
story.append(sp(8))

captions = [
    "Figure 1: Movies Tab — showing movie list with Add, Update, Delete, Search, Sort, and Add Show buttons",
    "Figure 2: Book Ticket Tab — movie and show dropdown, seat map showing all 15 seats (A1-C5)",
    "Figure 3: My Tickets Tab — ticket list showing T001 for Omkar / Bhaiyara, with Cancel, View Bill, Refresh",
    "Figure 4: Booking Confirmed Popup — ticket bill for Jaikishan Suthar, Avengers: Endgame, Seat B1, Rs.200",
]

for i, path in enumerate(screenshots[:4]):
    caption = captions[i] if i < len(captions) else f"Figure {i+1}: Application screenshot"
    story += add_image(path, caption, max_w=15*cm, max_h=7.5*cm)
    story.append(sp(4))

story.append(PageBreak())

# ══════════════════════════════════════════════════════
# SECTION 12 — TESTING
# ══════════════════════════════════════════════════════
story.append(H("12.  TESTING"))
story.append(sp(8))
story.append(P("The following test cases were manually tested on the running application:"))
story.append(sp(6))
story.append(make_table(
    ["Test Case", "Input", "Expected Output", "Result"],
    [
        ["Add new movie",          "Name: Avengers, Genre: Action, Duration: 181, Rating: 8.4",      "Movie added, shown in table with ID M001",       "✅ Pass"],
        ["Add movie — empty name", "Name: (blank)",                                                    "Error: Movie name cannot be empty",              "✅ Pass"],
        ["Update movie",           "ID: M001, New Rating: 9.0",                                       "Movie M001 rating updated to 9.0 in table",      "✅ Pass"],
        ["Delete movie",           "ID: M003",                                                         "Inception removed from list",                    "✅ Pass"],
        ["Search by name",         "Search: 'Avatar'",                                                 "Avatar row shown in table",                      "✅ Pass"],
        ["Sort by name",           "Click Sort by Name",                                               "Movies in A-Z order",                            "✅ Pass"],
        ["Sort by rating",         "Click Sort by Rating",                                             "Inception (8.8) shown first",                    "✅ Pass"],
        ["Add show",               "Movie M001, Time: 06:00 PM",                                      "Show S003 added to TreeMap, visible in dropdown", "✅ Pass"],
        ["Book ticket — valid",    "Name: Jaikishan, Phone: 9876543210, Seat: B1, Show: S003",        "Ticket T002 created, bill popup shown",           "✅ Pass"],
        ["Book same seat again",   "Same Seat B1 for same show",                                      "Warning: Seat B1 is already booked!",             "✅ Pass"],
        ["Book — empty name",      "Name: (blank)",                                                    "Error: Customer name cannot be empty",            "✅ Pass"],
        ["Book — invalid phone",   "Phone: 12345",                                                     "Error: Phone number must be 10 digits",          "✅ Pass"],
        ["Book — invalid seat",    "Seat: Z9",                                                         "Error: Invalid seat number: Z9",                 "✅ Pass"],
        ["Search ticket",          "Ticket ID: T001",                                                  "T001 details shown in ticket table",              "✅ Pass"],
        ["Search — not found",     "Ticket ID: T999",                                                  "Message: Ticket not found: T999",                "✅ Pass"],
        ["Cancel ticket",          "Ticket ID: T001 → Yes",                                           "Ticket removed, seat freed, booking list updated","✅ Pass"],
        ["View bill",              "Ticket ID: T002",                                                  "Formatted bill popup with all details",          "✅ Pass"],
    ],
    col_widths=[4*cm, 5*cm, 5.5*cm, 1*cm]
))

# ══════════════════════════════════════════════════════
# SECTION 13 — CONCLUSION
# ══════════════════════════════════════════════════════
story.append(sp(10))
story.append(H("13.  CONCLUSION"))
story.append(sp(8))
story.append(P("The <b>Movie Ticket Booking System</b> successfully demonstrates a complete, functional Java desktop application built using core Java concepts taught in the B.Tech CSE curriculum."))
story.append(sp(4))

conclusion_points = [
    "All 5 Java Collections (Array, ArrayList, LinkedList, HashMap, TreeMap) are clearly implemented and visible in BookingSystem.java.",
    "OOP principles — Encapsulation, Inheritance, Polymorphism, Constructors — are applied across all model and GUI classes.",
    "The GUI built with Java Swing provides a clean, working interface with Movies, Book Ticket, and My Tickets tabs.",
    "Exception handling and input validation ensure the application handles errors gracefully with user-friendly messages.",
    "CRUD operations are fully implemented for Movie management, and search/sort features are working correctly.",
    "The project is kept intentionally simple and student-level — easy to understand, explain in viva, and demonstrate live.",
]
for pt in conclusion_points:
    story.append(B(pt))

story.append(sp(8))
story.append(P("This project provided practical experience in applying Java programming concepts to build a real-world application, reinforcing classroom learning through hands-on development."))
story.append(sp(16))
story.append(hr())
story.append(sp(6))

sig = Table([
    [Paragraph("<b>Jaikishan Suthar</b>", S["body"]),
     Paragraph("<b>Roll No: 150096752152</b>", S["body"])],
    [Paragraph("B.Tech CSE", S["body"]),
     Paragraph("Java Programming Case Study", S["body"])],
], colWidths=[7.5*cm, 8*cm])
sig.setStyle(TableStyle([
    ("ALIGN", (0,0), (-1,-1), "LEFT"),
    ("TOPPADDING",(0,0),(-1,-1), 3),
]))
story.append(sig)

# ─── Build PDF ───────────────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    OUT,
    pagesize=A4,
    rightMargin=1.4*cm,
    leftMargin=1.4*cm,
    topMargin=1.5*cm,
    bottomMargin=1.2*cm,
    title="Movie Ticket Booking System Documentation",
    author="Jaikishan Suthar",
    subject="B.Tech CSE Java Programming Case Study",
)

doc.build(story,
          onFirstPage=on_cover,
          onLaterPages=on_page)

print(f"PDF generated: {OUT}")
