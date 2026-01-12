# Datastart Nitro

A starter template for building reactive web applications with **Sanic**, **Datastar**, and **Nitro**.

## Quick Start

### 1. Install Dependencies

```bash
uv sync
```

### 2. Initialize Tailwind CSS

```bash
nitro tw init
```

### 3. Start Development

Open two terminals:

**Terminal 1** - Start the Tailwind CSS watcher:
```bash
nitro tw dev
```

**Terminal 2** - Run the Sanic server:
```bash
python app.py
```

Visit `http://localhost:8000` in your browser.

## Tech Stack

- **[Sanic](https://sanic.dev/)** - Async Python web framework
- **[Datastar](https://data-star.dev/)** - Lightweight reactive framework
- **[Nitro](https://github.com/ndendic/nitro)** - Web development toolkit with Tailwind CSS CLI
- **[RustyTags](https://github.com/ndendic/RustyTags)** - High-performance HTML generation (Rust-powered)

## Project Structure

```
datastart_nitro/
├── app.py          # Main Sanic application
├── templates.py    # Base template and utilities
├── components.py   # Reusable UI components
├── static/         # Static assets (CSS, JS)
└── pyproject.toml  # Project dependencies
```

## Links

- [RustyTags](https://github.com/ndendic/RustyTags) - High-performance HTML generation library
- [Nitro](https://github.com/ndendic/nitro) - Full-stack web framework toolkit
- [Datastar](https://data-star.dev/) - Reactive component framework
- [Sanic](https://sanic.dev/) - Async web framework documentation
