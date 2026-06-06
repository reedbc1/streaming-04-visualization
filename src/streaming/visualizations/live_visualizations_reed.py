"""src/streaming/visualizations/live_visualizations_reed.py.

Project-specific live visualization functions used by the Kafka consumer.

This module creates a live bar chart of products sold by product name.
The chart opens in a window while the consumer is running and updates
as each message is consumed.

Author: Denise Case
Date: 2026-05

OBS:
  Don't edit this file - it should remain a working example.
  Copy it, rename it live_visualizations_yourname.py,
  and modify your copy for your own charts.
"""

# === DECLARE IMPORTS ===

from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt

# === DECLARE EXPORTS ===

# Use the built-in __all__ variable to declare a list of
# public objects that this module exports.
# This is a common Python convention that helps other developers understand
# which functions are intended for use outside this module.

__all__ = [
    "close_live_chart",
    "init_live_chart",
    "save_live_chart",
    "update_live_chart",
]


# === DEFINE LIVE CHART HELPERS ===


def init_live_chart() -> tuple[Any, Any, dict[str, int]]:
    """Create and show an empty live chart.

    Returns:
        A tuple of (figure, axis, product_counts).
    """
    # Matplotlib has a ion() function built in for "interactive ON" mode,
    # which allows the chart to update in real time as we modify it.
    # Call this function to turn on interactive mode.
    plt.ion()

    # Call subplots() to create a figure and axis for the chart.
    figure, axis = plt.subplots()

    # Initialize the running product tally.
    # This will be updated as messages are consumed.
    product_counts: dict[str, int] = {}

    # Set the title and axis labels for the chart.
    axis.set_title("Products Sold")
    axis.set_xlabel("Product")
    axis.set_ylabel("Units Sold")

    # Call the figure.show() method to display the chart window.
    figure.show()

    # Call the figure.canvas.draw() method to
    # ensure the chart is rendered and responsive.
    figure.canvas.draw()

    # Call the figure.canvas.flush_events() method to process any pending GUI events,
    # which helps the chart window to update properly.
    figure.canvas.flush_events()

    # Return the figure, axis, and the product tally for later use.
    return figure, axis, product_counts


def update_live_chart(
    *,
    figure: Any,
    axis: Any,
    product_counts: dict[str, int],
    message: dict[str, Any],
) -> None:
    """Update the live chart with one consumed message.

    All arguments after the asterisk (*) must be passed as keyword arguments.

    Arguments:
        figure: Matplotlib figure.
        axis: Matplotlib axis.
        product_counts: Running count of units sold by product name.
        message: One enriched Kafka message dictionary.

    Returns:
        None.
    """
    product_name = str(message["product_name"])
    quantity = int(message["quantity"])
    product_counts[product_name] = product_counts.get(product_name, 0) + quantity

    # Clear the axis
    axis.clear()

    # Re-plot the updated product counts as a bar chart.
    axis.bar(product_counts.keys(), product_counts.values())

    # Set the title and axis labels again after clearing the axis.
    axis.set_title("Products Sold")
    axis.set_xlabel("Product")
    axis.set_ylabel("Units Sold")
    axis.tick_params(axis="x", labelrotation=30)

    # Add a grid to the chart for better readability.
    axis.grid(True, axis="y")
    figure.tight_layout()

    # Call the figure.canvas.draw() method to update the chart with the new data.
    figure.canvas.draw()

    # Call the figure.canvas.flush_events() method to process any pending GUI events,
    # which helps the chart to update properly.
    figure.canvas.flush_events()

    # Call plt.pause() with a short time (e.g., 0.05 seconds) to allow the chart to update.
    plt.pause(0.05)


def save_live_chart(
    *,
    figure: Any,
    chart_path: Path,
) -> None:
    """Save the final live chart to an image file.

    All arguments after the asterisk (*) must be passed as keyword arguments.

    Arguments:
        figure: Matplotlib figure.
        chart_path: Output image path.

    Returns:
        None.
    """
    # Ensure the output directory exists before saving the figure.
    chart_path.parent.mkdir(parents=True, exist_ok=True)

    # Use the figure.savefig() method to save the chart to an image file.
    # Use the bbox_inches="tight" argument to ensure the saved image is cropped to the content of the chart.
    figure.savefig(chart_path, bbox_inches="tight")


def close_live_chart() -> None:
    """Turn off interactive chart mode."""
    # Call plt.ioff() to turn off interactive mode when the consumer is finished.
    plt.ioff()
