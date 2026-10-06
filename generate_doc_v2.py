#!/usr/bin/env python3
"""
PDF Documentation Generator for Movie Ticket Booking System
Student: Jaikishan Suthar | Roll No: 150096752152
"""

import base64, os, subprocess, sys

PROJECT_DIR = "/Users/jaikishansuthar/Desktop/movietickets"
OUTPUT_PDF  = os.path.join(PROJECT_DIR, "Movie_Ticket_Booking_System_Documentation.pdf")
SCREENSHOT  = os.path.join(PROJECT_DIR, "Screenshot 2026-09-29 at 10.44.55 AM.png")

# ── embed screenshot as base64 ──────────────────────────────────────────────
def img_tag(path, caption, width="88%"):
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = base64.b64encode(f.read()).decode()
        ext = "png"
        return f"""
        <figure>
          <img src="data:image/{ext};base64,{data}" style="width:{width};max-width:750px;
               display:block;margin:10px auto;border:1px solid #ccc;border-radius:6px;">
          <figcaption style="text-align:center;font-size:11px;color:#555;margin-top:4px;">{caption}</figcaption>
        </figure>"""
    return f"<p style='color:#999;font-style:italic;'>[ Screenshot not available: {os.path.basename(path)} ]</p>"

SS = img_tag(SCREENSHOT, "Figure 1 – Movie Ticket Booking System – Movies Tab")

# ── HTML ─────────────────────────────────────────────────────────────────────
HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  @page {{ size: A4; margin: 18mm 16mm 18mm 16mm; }}
  body {{ font-family: Arial, sans-serif; font-size: 11px; color: #1a1a2e; line-height: 1.5; }}

  /* ── cover ── */
  .cover {{
    height: 100vh; display:flex; flex-direction:column;
    justify-content:center; align-items:center; text-align:center;
    background: linear-gradient(160deg,#1e3c72 0%,#2a5298 60%,#1565c0 100%);
    color:#fff; page-break-after:always; padding:40px;
  }}
  .cover .badge {{
    background:rgba(255,255,255,0.18); border:1px solid rgba(255,255,255,0.4);
    border-radius:20px; padding:6px 20px; font-size:11px; letter-spacing:1px;
    text-transform:uppercase; margin-bottom:30px;
  }}
  .cover h1 {{ font-size:32px; font-weight:900; letter-spacing:1px; margin-bottom:10px; }}
  .cover h2 {{ font-size:16px; font-weight:400; opacity:0.85; margin-bottom:36px; }}
  .cover .divider {{ width:60px; height:3px; background:#ffd700; border-radius:2px; margin:0 auto 36px; }}
  .cover .info-box {{
    background:rgba(255,255,255,0.12); border:1px solid rgba(255,255,255,0.3);
    border-radius:10px; padding:20px 36px; margin-bottom:30px;
  }}
  .cover .info-box p {{ font-size:13px; margin:5px 0; }}
  .cover .info-box strong {{ font-size:15px; }}
  .cover .tags {{ display:flex; gap:10px; flex-wrap:wrap; justify-content:center; margin-top:10px; }}
  .cover .tag {{
    background:rgba(255,255,255,0.15); border:1px solid rgba(255,255,255,0.35);
    border-radius:12px; padding:4px 14px; font-size:10px;
  }}

  /* ── toc ── */
  .toc {{ page-break-after:always; padding:10px 0; }}
  .toc h2 {{ font-size:17px; color:#1e3c72; border-bottom:2px solid #1e3c72; padding-bottom:6px; margin-bottom:16px; }}
  .toc-item {{ display:flex; justify-content:space-between; padding:5px 0;
    border-bottom:1px dotted #ccc; font-size:11px; }}
  .toc-item .num {{ color:#1e3c72; font-weight:700; min-width:24px; }}
  .toc-item .title {{ flex:1; padding:0 8px; }}
  .toc-item .page {{ color:#888; }}

  /* ── sections ── */
  .section {{ page-break-before:always; padding-top:4px; }}
  .section-header {{
    background:linear-gradient(90deg,#1e3c72,#2a5298);
    color:#fff; padding:10px 16px; border-radius:6px; margin-bottom:14px;
    display:flex; align-items:center; gap:10px;
  }}
  .section-header .num {{
    background:rgba(255,255,255,0.25); border-radius:50%;
    width:28px; height:28px; display:flex; align-items:center; justify-content:center;
    font-weight:900; font-size:13px; flex-shrink:0;
  }}
  .section-header h2 {{ font-size:16px; font-weight:700; margin:0; }}

  h3 {{ font-size:12px; color:#1e3c72; margin:14px 0 6px; font-weight:700;
        border-left:3px solid #2a5298; padding-left:8px; }}

  p {{ margin-bottom:8px; font-size:11px; line-height:1.6; }}

  /* ── tables ── */
  table {{ width:100%; border-collapse:collapse; margin:10px 0 14px; font-size:10.5px; }}
  thead tr {{ background:#1e3c72; color:#fff; }}
  thead th {{ padding:7px 9px; text-align:left; font-size:10.5px; }}
  tbody tr:nth-child(even) {{ background:#eef2fb; }}
  tbody tr:hover {{ background:#dce6f7; }}
  tbody td {{ padding:6px 9px; border-bottom:1px solid #dce3f0; vertical-align:top; }}
  .badge-used {{ background:#1e7e34; color:#fff; padding:2px 8px; border-radius:10px; font-size:9.5px; }}
  .badge-no   {{ background:#6c757d; color:#fff; padding:2px 8px; border-radius:10px; font-size:9.5px; }}

  /* ── code block ── */
  code {{ background:#f0f4ff; padding:1px 5px; border-radius:3px; font-size:10px;
          font-family:'Courier New',monospace; color:#0d47a1; }}
  .code-block {{
    background:#0d1117; color:#e6edf3; padding:12px 16px; border-radius:6px;
    font-family:'Courier New',monospace; font-size:10px; line-height:1.6;
    margin:8px 0 12px; white-space:pre-wrap; word-break:break-word;
  }}
  .code-block .kw  {{ color:#ff7b72; }}
  .code-block .cl  {{ color:#79c0ff; }}
  .code-block .cm  {{ color:#8b949e; }}
  .code-block .str {{ color:#a5d6ff; }}

  /* ── flow diagram ── */
  .flow {{ display:flex; align-items:center; flex-wrap:wrap; gap:4px; margin:12px 0; }}
  .flow-box {{
    background:#1e3c72; color:#fff; padding:7px 12px; border-radius:6px;
    font-size:10px; font-weight:700; text-align:center; min-width:80px;
  }}
  .flow-arrow {{ color:#2a5298; font-size:18px; font-weight:900; }}

  /* ── info cards ── */
  .card-row {{ display:flex; gap:10px; margin:8px 0; }}
  .card {{
    flex:1; background:#f0f4ff; border-left:4px solid #1e3c72;
    border-radius:4px; padding:8px 10px; font-size:10.5px;
  }}
  .card strong {{ display:block; color:#1e3c72; margin-bottom:3px; }}

  /* ── footer/header for printed pages ── */
  @media print {{
    .cover {{ -webkit-print-color-adjust:exact; print-color-adjust:exact; }}
    .section-header {{ -webkit-print-color-adjust:exact; print-color-adjust:exact; }}
    thead tr {{ -webkit-print-color-adjust:exact; print-color-adjust:exact; }}
  }}

  figure {{ margin:10px 0; }}
  figcaption {{ text-align:center; font-size:10px; color:#666; margin-top:4px; }}
  img {{ max-width:100%; }}
</style>
</head>
<body>

<!-- ════════════════════════════════════════════════════════════════
     COVER PAGE
═════════════════════════════════════════════════════════════════ -->
<div class="cover">
  <div class="badge">B.Tech CSE — Java Programming Case Study</div>
  <h1>Movie Ticket Booking System</h1>
  <h2>A Java Swing Desktop Application</h2>
  <div class="divider"></div>
  <div class="info-box">
    <p>Submitted By</p>
    <p><strong>Jaikishan Suthar</strong></p>
    <p style="margin-top:8px;">Roll No: <strong>150096752152</strong></p>
    <p style="margin-top:4px; font-size:10px; opacity:0.8;">B.Tech Computer Science &amp; Engineering</p>
  </div>
  <div class="tags">
    <span class="tag">Java 17+</span>
    <span class="tag">Java Swing</span>
    <span class="tag">OOP</span>
    <span class="tag">Collections Framework</span>
    <span class="tag">Exception Handling</span>
    <span class="tag">CRUD</span>
  </div>
</div>

<!-- ════════════════════════════════════════════════════════════════
     TABLE OF CONTENTS
═════════════════════════════════════════════════════════════════ -->
<div class="toc">
  <h2>Table of Contents</h2>
  <div class="toc-item"><span class="num">1</span><span class="title">Case Study Introduction</span><span class="page">3</span></div>
  <div class="toc-item"><span class="num">2</span><span class="title">Technologies &amp; Java Features Used</span><span class="page">3</span></div>
  <div class="toc-item"><span class="num">3</span><span class="title">Project Structure</span><span class="page">4</span></div>
  <div class="toc-item"><span class="num">4</span><span class="title">Java File Explanation</span><span class="page">4</span></div>
  <div class="toc-item"><span class="num">5</span><span class="title">OOP Concepts Used</span><span class="page">6</span></div>
  <div class="toc-item"><span class="num">6</span><span class="title">Java Collections Used</span><span class="page">7</span></div>
  <div class="toc-item"><span class="num">7</span><span class="title">GUI Components Used</span><span class="page">8</span></div>
  <div class="toc-item"><span class="num">8</span><span class="title">Project Working Flow</span><span class="page">9</span></div>
  <div class="toc-item"><span class="num">9</span><span class="title">Screenshots</span><span class="page">9</span></div>
  <div class="toc-item"><span class="num">10</span><span class="title">Conclusion</span><span class="page">10</span></div>
</div>

<!-- ════════════════════════════════════════════════════════════════
     SECTION 1 — CASE STUDY INTRODUCTION
═════════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <div class="num">1</div>
    <h2>Case Study Introduction</h2>
  </div>

  <h3>What is the Movie Ticket Booking System?</h3>
  <p>
    The Movie Ticket Booking System is a desktop application built using Java and Java Swing.
    It allows a cinema to manage movies, show timings, seats, and ticket bookings — all from
    a single window on a computer.
  </p>

  <h3>What Problem Does It Solve?</h3>
  <p>
    Earlier, booking a movie ticket required standing in a long queue at the cinema counter.
    This application removes that problem by providing a simple digital system where the
    operator can add movies, create show timings, let customers select their seat, book a
    ticket, and get a printed bill — all in a few clicks.
  </p>

  <h3>What Have I Created?</h3>
  <div class="card-row">
    <div class="card"><strong>Movie Management</strong>Add, update, search and delete movies with details like name, genre, duration, and rating.</div>
    <div class="card"><strong>Show Management</strong>Create show timings for any movie. Shows are sorted automatically by time using TreeMap.</div>
  </div>
  <div class="card-row">
    <div class="card"><strong>Seat Booking</strong>View available seats (A1–C5 layout), select a seat, enter customer details, and confirm booking.</div>
    <div class="card"><strong>Ticket &amp; Billing</strong>Every booking generates a unique Ticket ID with a formatted bill showing price ₹200.</div>
  </div>

  <h3>Why Is It Useful?</h3>
  <p>
    This system demonstrates how Java's core features — Collections, OOP, Swing GUI, and
    Exception Handling — work together to build a complete, working desktop application.
    It is useful for a college lab, a small cinema, or as a practical demonstration of
    real-world Java programming concepts.
  </p>
</div>

<!-- ════════════════════════════════════════════════════════════════
     SECTION 2 — TECHNOLOGIES & JAVA FEATURES USED
═════════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <div class="num">2</div>
    <h2>Technologies &amp; Java Features Used</h2>
  </div>

  <table>
    <thead><tr><th>Technology / Feature</th><th>What It Is</th><th>How I Used It</th></tr></thead>
    <tbody>
      <tr><td><strong>Java 17+</strong></td><td>Core programming language</td><td>Entire application is written in Java</td></tr>
      <tr><td><strong>Java Swing</strong></td><td>Built-in Java GUI library</td><td>JFrame, JPanel, JTable, JButton, JComboBox, JOptionPane — all from Swing</td></tr>
      <tr><td><strong>OOP (Object-Oriented Programming)</strong></td><td>Class, Object, Encapsulation, Inheritance</td><td>Movie, Show, Customer, Ticket are separate classes with private fields and public methods</td></tr>
      <tr><td><strong>Java Collections Framework</strong></td><td>Ready-made data structures</td><td>ArrayList, LinkedList, HashMap, TreeMap — used in BookingSystem.java</td></tr>
      <tr><td><strong>Array</strong></td><td>Fixed-size collection</td><td><code>String[] seats</code> and <code>boolean[] seatBooked</code> in Show.java</td></tr>
      <tr><td><strong>Exception Handling</strong></td><td>try-catch, custom exceptions</td><td>SeatAlreadyBookedException, validation errors caught with try-catch</td></tr>
      <tr><td><strong>Validation</strong></td><td>Input checking before processing</td><td>Phone number (10 digits), empty name, empty movie name — checked before saving</td></tr>
      <tr><td><strong>CRUD Operations</strong></td><td>Create, Read, Update, Delete</td><td>Full CRUD for Movie; Create + Read for Customer, Show, Ticket</td></tr>
      <tr><td><strong>Searching</strong></td><td>Finding specific records</td><td>Movie search by name, Ticket search by ID (HashMap), Show search by ID</td></tr>
      <tr><td><strong>Sorting</strong></td><td>Ordering records</td><td><code>Collections.sort()</code> with <code>Comparator</code> — sort movies by name or rating</td></tr>
      <tr><td><strong>Event Handling</strong></td><td>Responding to button clicks</td><td><code>ActionListener</code> on every button in MoviePanel, BookingPanel, TicketPanel</td></tr>
    </tbody>
  </table>
</div>

<!-- ════════════════════════════════════════════════════════════════
     SECTION 3 — PROJECT STRUCTURE
═════════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <div class="num">3</div>
    <h2>Project Structure</h2>
  </div>

  <div class="code-block"><span class="cm">MovieTicketBookingSystem/</span>
│
├── src/
│   ├── model/
│   │   ├── Movie.java                  <span class="cm">← Stores movie details</span>
│   │   ├── Show.java                   <span class="cm">← Stores show + seat data</span>
│   │   ├── Customer.java               <span class="cm">← Stores customer info</span>
│   │   ├── Ticket.java                 <span class="cm">← Stores booking + bill</span>
│   │   └── SeatAlreadyBookedException.java  <span class="cm">← Custom exception</span>
│   │
│   ├── service/
│   │   └── BookingSystem.java          <span class="cm">← All logic + all collections</span>
│   │
│   ├── gui/
│   │   ├── MainFrame.java              <span class="cm">← Main window + tabs</span>
│   │   ├── MoviePanel.java             <span class="cm">← Movie CRUD tab</span>
│   │   ├── BookingPanel.java           <span class="cm">← Book Ticket tab</span>
│   │   └── TicketPanel.java            <span class="cm">← My Tickets tab</span>
│   │
│   └── Main.java                       <span class="cm">← Entry point</span>
│
├── README.md
└── .gitignore

<span class="cm">Total Java files: 11  (within the 8–12 student limit)</span></div>
</div>

<!-- ════════════════════════════════════════════════════════════════
     SECTION 4 — JAVA FILE EXPLANATION
═════════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <div class="num">4</div>
    <h2>Java File Explanation</h2>
  </div>

  <h3>Quick Reference Table</h3>
  <table>
    <thead><tr><th>File Name</th><th>Class Name</th><th>Package</th><th>Purpose</th></tr></thead>
    <tbody>
      <tr><td><code>Main.java</code></td><td><code>Main</code></td><td>default</td><td>Application entry point — starts the Swing GUI on the Event Dispatch Thread</td></tr>
      <tr><td><code>Movie.java</code></td><td><code>Movie</code></td><td>model</td><td>Stores movieId, movieName, genre, duration, rating</td></tr>
      <tr><td><code>Show.java</code></td><td><code>Show</code></td><td>model</td><td>Stores show details + seat array; handles bookSeat / cancelSeat</td></tr>
      <tr><td><code>Customer.java</code></td><td><code>Customer</code></td><td>model</td><td>Stores customer info with static phone/name validation methods</td></tr>
      <tr><td><code>Ticket.java</code></td><td><code>Ticket</code></td><td>model</td><td>Stores booking details; generates a formatted bill string</td></tr>
      <tr><td><code>SeatAlreadyBookedException.java</code></td><td><code>SeatAlreadyBookedException</code></td><td>model</td><td>Custom checked exception thrown when a booked seat is selected again</td></tr>
      <tr><td><code>BookingSystem.java</code></td><td><code>BookingSystem</code></td><td>service</td><td>Central service — holds all 5 collections + all business methods</td></tr>
      <tr><td><code>MainFrame.java</code></td><td><code>MainFrame</code></td><td>gui</td><td>JFrame with 3 tabs + header + Exit button; creates shared BookingSystem</td></tr>
      <tr><td><code>MoviePanel.java</code></td><td><code>MoviePanel</code></td><td>gui</td><td>Movies tab — Add/Update/Delete/Search/Sort/AddShow buttons + JTable</td></tr>
      <tr><td><code>BookingPanel.java</code></td><td><code>BookingPanel</code></td><td>gui</td><td>Book Ticket tab — movie/show dropdowns, customer form, seat view, book</td></tr>
      <tr><td><code>TicketPanel.java</code></td><td><code>TicketPanel</code></td><td>gui</td><td>My Tickets tab — search, cancel, view bill for any ticket</td></tr>
    </tbody>
  </table>

  <h3>Main.java</h3>
  <p><strong>Purpose:</strong> This is the starting point of the application. It uses
  <code>SwingUtilities.invokeLater()</code> to launch <code>MainFrame</code> on the
  Swing Event Dispatch Thread (EDT) — the correct and safe way to start a Swing app.</p>
  <div class="code-block"><span class="kw">public class</span> <span class="cl">Main</span> {{
    <span class="kw">public static void</span> main(String[] args) {{
        SwingUtilities.invokeLater(() -&gt; <span class="kw">new</span> <span class="cl">MainFrame</span>());
    }}
}}</div>

  <h3>Movie.java</h3>
  <p><strong>Important variables:</strong> <code>movieId</code>, <code>movieName</code>,
  <code>genre</code>, <code>duration</code> (int), <code>rating</code> (double).<br>
  <strong>Important methods:</strong> constructor, getters (<code>getMovieId()</code> etc.),
  setters (<code>setMovieName()</code> etc.), <code>toString()</code> returning a pipe-separated line.<br>
  <strong>Viva line:</strong> "Movie.java is a model class that stores the details of one movie using
  private fields and provides public getter and setter methods — this is encapsulation."</p>

  <h3>Show.java</h3>
  <p><strong>Important variables:</strong> <code>String[] seats</code> (15 fixed seat names A1–C5),
  <code>boolean[] seatBooked</code> (tracks which seats are booked), <code>Movie movie</code>,
  <code>String showTime</code>.<br>
  <strong>Important methods:</strong> <code>isSeatAvailable()</code>, <code>bookSeat()</code>
  (throws Exception if already booked), <code>cancelSeat()</code>, <code>getAllSeatsInfo()</code>.<br>
  <strong>Viva line:</strong> "Show.java uses two parallel arrays — seats[] for seat names and
  seatBooked[] for their availability — to track the cinema seating layout."</p>

  <h3>Customer.java</h3>
  <p><strong>Important variables:</strong> <code>customerId</code>, <code>name</code>,
  <code>phone</code>, <code>email</code>.<br>
  <strong>Important methods:</strong> <code>isValidPhone(String)</code> — static method using
  regex <code>\\d{{10}}</code> to verify 10-digit phone; <code>isValidName(String)</code> — checks
  non-empty.<br>
  <strong>Viva line:</strong> "Customer.java includes static validation methods so I can validate
  input before creating a Customer object."</p>

  <h3>Ticket.java</h3>
  <p><strong>Important variables:</strong> <code>ticketId</code>, <code>Customer customer</code>,
  <code>Movie movie</code>, <code>Show show</code>, <code>seatNumber</code>, <code>price</code> (200.0).<br>
  <strong>Important methods:</strong> <code>getBillInfo()</code> — returns a formatted multi-line
  bill string; <code>toString()</code> — single-line summary.<br>
  <strong>Viva line:</strong> "Ticket.java connects Customer, Movie, and Show objects together,
  showing object composition in OOP."</p>

  <h3>SeatAlreadyBookedException.java</h3>
  <p><strong>Purpose:</strong> A custom checked exception that extends <code>Exception</code>.
  It is thrown specifically when a user tries to book a seat that is already taken, giving
  a meaningful, specific error message instead of a generic one.<br>
  <strong>Viva line:</strong> "SeatAlreadyBookedException extends Exception — this is inheritance.
  I call super(message) to pass the error message to the parent Exception class."</p>

  <h3>BookingSystem.java</h3>
  <p><strong>Purpose:</strong> This is the service class that holds all the data (all 5 collections)
  and all the application logic. GUI panels do not do any logic themselves — they call BookingSystem
  methods.<br>
  <strong>Important variables:</strong>
  <code>ArrayList&lt;Movie&gt; movies</code>, <code>ArrayList&lt;Customer&gt; customers</code>,
  <code>LinkedList&lt;Ticket&gt; bookingList</code>, <code>HashMap&lt;String, Ticket&gt; tickets</code>,
  <code>TreeMap&lt;String, Show&gt; shows</code>.<br>
  <strong>Important methods:</strong> <code>addMovie()</code>, <code>updateMovie()</code>,
  <code>deleteMovie()</code>, <code>searchMovie()</code>, <code>addCustomer()</code>,
  <code>addShow()</code>, <code>bookTicket()</code>, <code>cancelTicket()</code>,
  <code>searchTicket()</code>, <code>getMoviesSortedByName()</code>,
  <code>getMoviesSortedByRating()</code>.<br>
  <strong>Viva line:</strong> "BookingSystem.java is my service class — it is the brain of the
  application. All collections and all methods live here."</p>

  <h3>MainFrame.java</h3>
  <p><strong>Purpose:</strong> Creates the main JFrame window (900×600). Adds a blue header label,
  a JTabbedPane with 3 tabs (Movies, Book Ticket, My Tickets), and a red Exit button in the footer.
  Creates one shared <code>BookingSystem</code> object and passes it to all three panels.<br>
  <strong>Viva line:</strong> "MainFrame extends JFrame — it is the main window. I pass one
  BookingSystem object to all panels so they share the same data."</p>

  <h3>MoviePanel.java</h3>
  <p><strong>Purpose:</strong> The Movies tab. Lets the user add, update, delete, search, and
  sort movies. Also has an "Add Show for Movie" button. Displays movies in a <code>JTable</code>.
  Clicking a row auto-fills the Movie ID field using a <code>ListSelectionListener</code>.<br>
  <strong>Viva line:</strong> "MoviePanel contains the full CRUD for movies — Add, Update, Delete,
  and Search — all through buttons that call BookingSystem methods."</p>

  <h3>BookingPanel.java</h3>
  <p><strong>Purpose:</strong> The Book Ticket tab. Has a JComboBox for movies, a JComboBox for
  shows (loaded dynamically when movie changes via <code>ActionListener</code>), text fields for
  customer details, and a seat view area. Calls <code>bookingSystem.bookTicket()</code> and
  shows the bill in JOptionPane on success.<br>
  <strong>Viva line:</strong> "BookingPanel shows the seat map and calls bookTicket() — it handles
  both SeatAlreadyBookedException and generic Exception separately with two catch blocks."</p>

  <h3>TicketPanel.java</h3>
  <p><strong>Purpose:</strong> The My Tickets tab. Shows all booked tickets in a JTable (iterates
  over LinkedList). Allows search by Ticket ID (HashMap lookup), cancel ticket (frees the seat),
  and View Bill (shows formatted bill in JOptionPane).<br>
  <strong>Viva line:</strong> "TicketPanel uses the LinkedList to display all tickets in booking
  order, and the HashMap to do fast search and cancellation by Ticket ID."</p>
</div>

<!-- ════════════════════════════════════════════════════════════════
     SECTION 5 — OOP CONCEPTS USED
═════════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <div class="num">5</div>
    <h2>OOP Concepts Used</h2>
  </div>

  <table>
    <thead><tr><th>OOP Concept</th><th>Used?</th><th>File / Class</th><th>Example from My Project</th></tr></thead>
    <tbody>
      <tr>
        <td><strong>Class</strong></td>
        <td><span class="badge-used">Used</span></td>
        <td>All 11 files</td>
        <td>Every file defines a class: <code>class Movie</code>, <code>class BookingSystem</code>, etc.</td>
      </tr>
      <tr>
        <td><strong>Object</strong></td>
        <td><span class="badge-used">Used</span></td>
        <td>BookingSystem.java, MainFrame.java</td>
        <td><code>new Movie(...)</code>, <code>new Show(...)</code>, <code>new Ticket(...)</code>, <code>new BookingSystem()</code> — objects created throughout</td>
      </tr>
      <tr>
        <td><strong>Encapsulation</strong></td>
        <td><span class="badge-used">Used</span></td>
        <td>Movie.java, Customer.java, Show.java, Ticket.java</td>
        <td>All fields are <code>private</code>. External access only through <code>public</code> getters/setters (e.g. <code>getMovieName()</code>, <code>setMovieName()</code>)</td>
      </tr>
      <tr>
        <td><strong>Constructor</strong></td>
        <td><span class="badge-used">Used</span></td>
        <td>All model classes</td>
        <td><code>public Movie(String movieId, String movieName, String genre, int duration, double rating)</code> — sets all fields on object creation</td>
      </tr>
      <tr>
        <td><strong>Inheritance</strong></td>
        <td><span class="badge-used">Used</span></td>
        <td>SeatAlreadyBookedException.java, MainFrame.java, all Panel classes</td>
        <td><code>SeatAlreadyBookedException extends Exception</code>; <code>MainFrame extends JFrame</code>; <code>MoviePanel extends JPanel</code></td>
      </tr>
      <tr>
        <td><strong>Method Overriding</strong></td>
        <td><span class="badge-used">Used</span></td>
        <td>All model classes</td>
        <td><code>@Override toString()</code> in Movie, Show, Customer, Ticket — overrides Object's default toString</td>
      </tr>
      <tr>
        <td><strong>Abstraction</strong></td>
        <td><span class="badge-no">Not directly</span></td>
        <td>—</td>
        <td>No abstract class or interface defined. BookingSystem provides logical abstraction (hides logic from GUI) but no Java <code>abstract</code> keyword is used.</td>
      </tr>
      <tr>
        <td><strong>Polymorphism</strong></td>
        <td><span class="badge-no">Not directly</span></td>
        <td>—</td>
        <td>No method overloading or interface polymorphism. Exception catching uses Java's built-in polymorphic dispatch (<code>catch(Exception e)</code>).</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ════════════════════════════════════════════════════════════════
     SECTION 6 — JAVA COLLECTIONS USED
═════════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <div class="num">6</div>
    <h2>Java Collections Used</h2>
  </div>

  <p>All five collections are declared and used in <strong>BookingSystem.java</strong>.
  They are easy to find — they are the first five field declarations at the top of that class.</p>

  <table>
    <thead><tr><th>Collection</th><th>Variable Name (exact)</th><th>What It Stores</th><th>Why This Type</th></tr></thead>
    <tbody>
      <tr>
        <td><strong>Array</strong></td>
        <td><code>String[] seats</code><br><code>boolean[] seatBooked</code></td>
        <td>Fixed 15 seat names (A1–C5) and their booked/free status</td>
        <td>Seat count is fixed (15), so a fixed-size array is the right choice. Used in <strong>Show.java</strong></td>
      </tr>
      <tr>
        <td><strong>ArrayList&lt;Movie&gt;</strong></td>
        <td><code>movies</code></td>
        <td>All movies in the system</td>
        <td>Dynamic size — movies can be added/deleted. Supports index-based access. Used in <code>addMovie()</code>, <code>deleteMovie()</code>, <code>getMovies()</code></td>
      </tr>
      <tr>
        <td><strong>ArrayList&lt;Customer&gt;</strong></td>
        <td><code>customers</code></td>
        <td>All registered customers</td>
        <td>Same reason as movies — grows dynamically. Used in <code>addCustomer()</code>, <code>getCustomers()</code></td>
      </tr>
      <tr>
        <td><strong>LinkedList&lt;Ticket&gt;</strong></td>
        <td><code>bookingList</code></td>
        <td>All booked tickets in booking order</td>
        <td>Preserves insertion order — first booked appears first. Efficient add/remove. Used in <code>bookTicket()</code>, <code>cancelTicket()</code>, <code>getBookingList()</code></td>
      </tr>
      <tr>
        <td><strong>HashMap&lt;String, Ticket&gt;</strong></td>
        <td><code>tickets</code></td>
        <td>Tickets with Ticket ID as key (T001, T002, …)</td>
        <td>O(1) lookup — <code>tickets.get("T001")</code> finds the ticket instantly without looping. Used in <code>searchTicket()</code>, <code>cancelTicket()</code></td>
      </tr>
      <tr>
        <td><strong>TreeMap&lt;String, Show&gt;</strong></td>
        <td><code>shows</code></td>
        <td>All shows, key = showTime + "_" + showId</td>
        <td>Automatically keeps shows sorted by time — no extra sort code needed. Used in <code>addShow()</code>, <code>getShows()</code>, <code>getShowsForMovie()</code></td>
      </tr>
    </tbody>
  </table>

  <h3>Where to Point in the Code (for Viva)</h3>
  <div class="code-block"><span class="cm">// BookingSystem.java — top of the class — show these 5 lines:</span>
<span class="kw">private</span> ArrayList&lt;Movie&gt;       movies      = <span class="kw">new</span> ArrayList&lt;&gt;();
<span class="kw">private</span> ArrayList&lt;Customer&gt;    customers   = <span class="kw">new</span> ArrayList&lt;&gt;();
<span class="kw">private</span> LinkedList&lt;Ticket&gt;     bookingList = <span class="kw">new</span> LinkedList&lt;&gt;();
<span class="kw">private</span> HashMap&lt;String, Ticket&gt; tickets    = <span class="kw">new</span> HashMap&lt;&gt;();
<span class="kw">private</span> TreeMap&lt;String, Show&gt;   shows      = <span class="kw">new</span> TreeMap&lt;&gt;();</div>

  <h3>Sorting with Collections.sort() and Comparator</h3>
  <div class="code-block"><span class="cm">// BookingSystem.java — getMoviesSortedByName()</span>
Collections.sort(sorted, Comparator.comparing(Movie::getMovieName));

<span class="cm">// BookingSystem.java — getMoviesSortedByRating() (highest first)</span>
sorted.sort((m1, m2) -&gt; Double.compare(m2.getRating(), m1.getRating()));</div>
</div>

<!-- ════════════════════════════════════════════════════════════════
     SECTION 7 — GUI COMPONENTS USED
═════════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <div class="num">7</div>
    <h2>GUI Components Used (Java Swing)</h2>
  </div>

  <table>
    <thead><tr><th>Component</th><th>What It Does</th><th>Where Used in My Project</th></tr></thead>
    <tbody>
      <tr><td><code>JFrame</code></td><td>The main window of the application</td><td><code>MainFrame extends JFrame</code> — the 900×600 main window</td></tr>
      <tr><td><code>JPanel</code></td><td>A container that groups other components</td><td>Used in all GUI classes for form panels, button panels, seat panels</td></tr>
      <tr><td><code>JTabbedPane</code></td><td>Shows multiple tabs in one window</td><td><code>MainFrame.java</code> — Movies / Book Ticket / My Tickets tabs</td></tr>
      <tr><td><code>JLabel</code></td><td>Displays text on screen</td><td>All panels — field labels like "Movie Name:", "Select Show:", header text</td></tr>
      <tr><td><code>JTextField</code></td><td>Single-line text input box</td><td>MoviePanel (name, genre, duration, rating), BookingPanel (customer name, phone, email, seat)</td></tr>
      <tr><td><code>JButton</code></td><td>Clickable button</td><td>All panels — Add Movie, Book Ticket, Cancel, Search, Exit, etc.</td></tr>
      <tr><td><code>JComboBox</code></td><td>Dropdown selection</td><td><code>BookingPanel.java</code> — <code>cmbMovie</code> (select movie) and <code>cmbShow</code> (select show)</td></tr>
      <tr><td><code>JTable</code></td><td>Displays data in rows and columns</td><td><code>MoviePanel.java</code> (movie list), <code>TicketPanel.java</code> (ticket list)</td></tr>
      <tr><td><code>DefaultTableModel</code></td><td>Controls data in JTable</td><td>MoviePanel and TicketPanel — <code>tableModel.addRow()</code>, <code>setRowCount(0)</code></td></tr>
      <tr><td><code>JScrollPane</code></td><td>Adds scroll bars to a component</td><td>Wraps JTable in MoviePanel and TicketPanel; wraps seat text area in BookingPanel</td></tr>
      <tr><td><code>JTextArea</code></td><td>Multi-line text display</td><td><code>BookingPanel.java</code> — <code>txtAvailableSeats</code> shows the seat map</td></tr>
      <tr><td><code>JOptionPane</code></td><td>Pop-up dialog boxes</td><td>Success/error messages, bill display, delete confirmation, exit confirmation — everywhere</td></tr>
      <tr><td><code>BorderLayout</code></td><td>Positions items: NORTH/CENTER/SOUTH</td><td>MainFrame, MoviePanel, BookingPanel, TicketPanel — outer layout</td></tr>
      <tr><td><code>GridLayout</code></td><td>Equal-sized grid of cells</td><td>Form panels in MoviePanel (3×4 grid) and BookingPanel (8×2 grid)</td></tr>
      <tr><td><code>FlowLayout</code></td><td>Arranges items left-to-right in a row</td><td>Button panels in all three GUI classes</td></tr>
      <tr><td><code>ActionListener</code></td><td>Responds to button clicks / dropdown changes</td><td>Every button uses <code>btnAdd.addActionListener(e -&gt; addMovie())</code>; cmbMovie uses it to reload shows</td></tr>
      <tr><td><code>ListSelectionListener</code></td><td>Responds to row selection in JTable</td><td><code>MoviePanel.java</code> — clicking a movie row auto-fills the Movie ID field</td></tr>
      <tr><td><code>ChangeListener</code></td><td>Responds to tab switching</td><td><code>MainFrame.java</code> — refreshes panel data when user switches tabs</td></tr>
    </tbody>
  </table>
</div>

<!-- ════════════════════════════════════════════════════════════════
     SECTION 8 — PROJECT WORKING FLOW
═════════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <div class="num">8</div>
    <h2>Project Working Flow</h2>
  </div>

  <div class="flow">
    <div class="flow-box">Main.java</div>
    <div class="flow-arrow">→</div>
    <div class="flow-box">MainFrame</div>
    <div class="flow-arrow">→</div>
    <div class="flow-box">BookingSystem created</div>
    <div class="flow-arrow">→</div>
    <div class="flow-box">Sample data loaded</div>
    <div class="flow-arrow">→</div>
    <div class="flow-box">3 Tabs visible</div>
  </div>

  <h3>Step-by-Step Flow</h3>
  <table>
    <thead><tr><th>Step</th><th>What Happens</th><th>Class / Method Involved</th></tr></thead>
    <tbody>
      <tr><td><strong>1. App Start</strong></td><td><code>Main.java</code> calls <code>new MainFrame()</code> via SwingUtilities</td><td>Main.java → MainFrame.java</td></tr>
      <tr><td><strong>2. GUI Setup</strong></td><td>MainFrame creates BookingSystem, creates 3 panels, adds them to tabs</td><td>MainFrame → BookingSystem, MoviePanel, BookingPanel, TicketPanel</td></tr>
      <tr><td><strong>3. Sample Data</strong></td><td>4 movies (Avengers, Avatar, Inception, Interstellar) and 4 shows are added automatically</td><td>BookingSystem.loadSampleData()</td></tr>
      <tr><td><strong>4. Add Movie</strong></td><td>User fills form → clicks Add Movie → BookingSystem.addMovie() → ArrayList grows → table refreshes</td><td>MoviePanel → BookingSystem.addMovie()</td></tr>
      <tr><td><strong>5. Add Show</strong></td><td>User selects a movie row → clicks "Add Show for Movie" → enters time → show added to TreeMap</td><td>MoviePanel.addShowForMovie() → BookingSystem.addShow()</td></tr>
      <tr><td><strong>6. Book Ticket</strong></td><td>User selects movie + show → enters name/phone/email/seat → clicks Book Ticket</td><td>BookingPanel.bookTicket() → BookingSystem.bookTicket()</td></tr>
      <tr><td><strong>7. Validation</strong></td><td>Empty name / invalid phone / booked seat → exception thrown → JOptionPane error shown</td><td>BookingSystem.bookTicket() → SeatAlreadyBookedException / Exception</td></tr>
      <tr><td><strong>8. Ticket Created</strong></td><td>New Ticket object → stored in HashMap (fast lookup) + LinkedList (order) → bill shown in popup</td><td>Ticket.java, tickets.put(), bookingList.add()</td></tr>
      <tr><td><strong>9. View Tickets</strong></td><td>My Tickets tab → refreshTable() iterates LinkedList → fills JTable</td><td>TicketPanel.refreshTable() → bookingSystem.getBookingList()</td></tr>
      <tr><td><strong>10. Search Ticket</strong></td><td>Enter Ticket ID → searchTicket() → HashMap.get() → O(1) lookup → show in table</td><td>TicketPanel → BookingSystem.searchTicket() → tickets.get()</td></tr>
      <tr><td><strong>11. Cancel Ticket</strong></td><td>Ticket found → show.cancelSeat() frees seat → removed from HashMap + LinkedList</td><td>BookingSystem.cancelTicket()</td></tr>
      <tr><td><strong>12. View Bill</strong></td><td>Ticket.getBillInfo() returns formatted string → shown in JOptionPane</td><td>Ticket.getBillInfo() → JOptionPane.showMessageDialog()</td></tr>
    </tbody>
  </table>
</div>

<!-- ════════════════════════════════════════════════════════════════
     SECTION 9 — SCREENSHOTS
═════════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <div class="num">9</div>
    <h2>Screenshots</h2>
  </div>

  <h3>Application Overview</h3>
  {SS}

  <h3>What the Application Shows</h3>
  <table>
    <thead><tr><th>Tab / Screen</th><th>What You See</th><th>Key Features Visible</th></tr></thead>
    <tbody>
      <tr>
        <td><strong>Movies Tab</strong></td>
        <td>List of all movies in a JTable with columns: Movie ID, Movie Name, Genre, Duration, Rating</td>
        <td>Add Movie, Update, Delete, Search, Add Show for Movie, Sort by Name/Rating, Refresh — 8 colour-coded buttons</td>
      </tr>
      <tr>
        <td><strong>Book Ticket Tab</strong></td>
        <td>Left side: booking form (movie dropdown, show dropdown, customer fields, seat input). Right side: seat map showing A1–C5 grid</td>
        <td>Shows booked seats as [A1]; available seats as A1. Three buttons: Book Ticket (green), Clear (grey), Refresh Movies (blue)</td>
      </tr>
      <tr>
        <td><strong>My Tickets Tab</strong></td>
        <td>Table of all booked tickets with columns: Ticket ID, Customer, Movie, Show Time, Seat, Price</td>
        <td>Search by Ticket ID, Cancel Ticket, View Bill — bill shown in a popup with formatted layout</td>
      </tr>
      <tr>
        <td><strong>Bill Popup</strong></td>
        <td>JOptionPane showing the full bill: Ticket ID, Customer name, Movie, Show Time, Seat, Price ₹200, Total</td>
        <td>Generated by Ticket.getBillInfo() method</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- ════════════════════════════════════════════════════════════════
     SECTION 10 — CONCLUSION
═════════════════════════════════════════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <div class="num">10</div>
    <h2>Conclusion</h2>
  </div>

  <p>
    The Movie Ticket Booking System is a complete Java desktop application built as a
    B.Tech CSE Java Programming case study. The project successfully demonstrates all
    the required Java concepts in a simple, working, and easy-to-understand way.
  </p>

  <h3>What I Learned</h3>
  <table>
    <thead><tr><th>Concept</th><th>What I Applied</th></tr></thead>
    <tbody>
      <tr><td><strong>OOP</strong></td><td>Designed separate classes (Movie, Show, Customer, Ticket) with encapsulation, constructors, and method overriding</td></tr>
      <tr><td><strong>Collections Framework</strong></td><td>Used 5 different collections — each chosen for a specific reason (ArrayList for movies, HashMap for fast ticket lookup, TreeMap for sorted shows)</td></tr>
      <tr><td><strong>Java Swing</strong></td><td>Built a fully working GUI with JFrame, JTabbedPane, JTable, JComboBox, JOptionPane — no external library needed</td></tr>
      <tr><td><strong>Exception Handling</strong></td><td>Created a custom exception (SeatAlreadyBookedException) and used try-catch blocks with meaningful error messages</td></tr>
      <tr><td><strong>CRUD + Search + Sort</strong></td><td>Full CRUD for movies; search by ID and name; sort by name and rating using Collections.sort() and Comparator</td></tr>
      <tr><td><strong>Validation</strong></td><td>Validated phone (10 digits regex), empty names, seat existence, duplicate booking — all before any data is saved</td></tr>
    </tbody>
  </table>

  <p style="margin-top:14px;">
    Through this project I gained practical experience of how Java's core features work together
    to build a real application — not just in theory, but as a complete, runnable program that
    can be demonstrated and explained step by step.
  </p>

  <div style="margin-top:28px; border-top:1px solid #ccc; padding-top:14px; display:flex; justify-content:space-between; font-size:11px; color:#555;">
    <div>
      <strong style="font-size:12px;">Jaikishan Suthar</strong><br>
      Roll No: 150096752152<br>
      B.Tech CSE
    </div>
    <div style="text-align:right;">
      <strong>Movie Ticket Booking System</strong><br>
      Java Programming Case Study<br>
      October 2026
    </div>
  </div>
</div>

</body>
</html>"""

# ── write HTML ────────────────────────────────────────────────────────────────
html_path = os.path.join(PROJECT_DIR, "_doc_v2_temp.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(HTML)
print(f"HTML written: {html_path}")

# ── convert to PDF ────────────────────────────────────────────────────────────
# Try wkhtmltopdf first, then weasyprint, then chromium
converters = [
    ["wkhtmltopdf",
     "--page-size", "A4",
     "--margin-top",    "15mm",
     "--margin-bottom", "15mm",
     "--margin-left",   "14mm",
     "--margin-right",  "14mm",
     "--encoding", "UTF-8",
     "--enable-local-file-access",
     "--no-outline",
     html_path, OUTPUT_PDF],
]

# chromium / chrome headless
for chrome_bin in ["chromium", "chromium-browser", "google-chrome",
                   "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                   "/usr/bin/google-chrome"]:
    converters.append([
        chrome_bin,
        "--headless", "--disable-gpu",
        "--no-sandbox",
        "--print-to-pdf=" + OUTPUT_PDF,
        "--print-to-pdf-no-header",
        "file://" + html_path
    ])

success = False
for cmd in converters:
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if r.returncode == 0 and os.path.exists(OUTPUT_PDF) and os.path.getsize(OUTPUT_PDF) > 5000:
            print(f"PDF generated with: {cmd[0]}")
            success = True
            break
    except (FileNotFoundError, subprocess.TimeoutExpired):
        continue

if not success:
    # weasyprint fallback (pure Python)
    try:
        import weasyprint
        weasyprint.HTML(filename=html_path).write_pdf(OUTPUT_PDF)
        if os.path.exists(OUTPUT_PDF) and os.path.getsize(OUTPUT_PDF) > 5000:
            print("PDF generated with weasyprint")
            success = True
    except Exception as e:
        print(f"weasyprint failed: {e}")

if success:
    size_kb = os.path.getsize(OUTPUT_PDF) // 1024
    print(f"SUCCESS: {OUTPUT_PDF}  ({size_kb} KB)")
else:
    print("All converters failed. Install wkhtmltopdf or Google Chrome.")
    print(f"HTML is at: {html_path}")

# clean up temp HTML
try:
    os.remove(html_path)
except:
    pass
