# 🪵 Python Logger Suite

This repository provides a modular Python setup for logging and log viewing — from simple file-based loggers to WebSocket-enabled viewers.

## 📦 Components

- `paths.py` – Centralized file path management
  * Defines placeholders for log and data directories
  * Enables unified path referencing across the codebase
  * Avoids hardcoded values for improved maintainability
  * Purpose: Provides a scalable foundation for managing paths – can be extended dynamically using environment variables or config files.
- `logger_setup.py` – A central utility for initializing and managing logging
  * Initializes logger with configurable name and level
  * Logs to both console and file (LOG_PATH)
  * Applies consistent formatting to all outputs
  * Prevents duplicate handlers when logger already exists
  * Purpose: Enhances debugging and observability without cluttering main application logic.
- `sample_logger.py` – Application entry point using the logging tools
  * Imports init_logger from logger_setup
  * Initializes logger with level (Customize as required)
  * Purpose: Validates logger configuration and serves as a template for other modules.
- `log_html_live.py` – Minimal Flask application to stream full log contents with periodic refresh
  * Reads the complete log file on each request
  * Renders logs in terminal-style formatted HTML page
  * Auto-refreshes every 2 seconds via meta tag
  * Purpose: Simple yet effective log monitoring for quick setups without real-time sockets.
- `log_html_with_filter.py` – Lightweight Flask app for displaying logs
  * Reads log file in reverse order (latest entries first)
  * Supports log-level filtering (ERROR, WARNING, INFO, DEBUG)
  * Renders HTML output with color-coded log types
  * Purpose: Allows quick activity monitoring without manual file access.
- `log_html_websocket.py` – Flask-based app with WebSocket support for live log streaming
  * Uses Flask-SocketIO for real-time communication
  * Streams tail-end of log file updates to connected clients
  * Displays logs in styled HTML interface based on severity (error, warning, info)
  * Includes status indicator and “Stop Monitor” button
  * Purpose: Provides real-time insights into application behavior for development and operations.
- `project.log` – Included sample log file for testing and demo purposes
  * Serves as log target for multiple viewer tools
  * Enables immediate validation of logging pipeline
  * Content may be temporary or example-based; can be cleared or rotated
  * Note: In production, this file is typically excluded via .gitignore or managed separately to prevent log overflow.

## 💡 Features

- ✅ Centralized path management
- ✅ Customizable logger setup
- ✅ Exception handling and fallback
- ✅ Modular log viewers
- ✅ Real-time WebSocket integration
- ✅ Easily extendable for test grouping and nested log structure

## 📁 How to use

```bash
# Clone the repo
git clone https://github.com/yourusername/logger-project

# Run the main application
python main.py
