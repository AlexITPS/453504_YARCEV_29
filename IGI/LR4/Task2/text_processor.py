"""
Purpose: Core models for text processing using inheritance and mixins.
LW 4 (Task 2)
Version 1.0
"""

from abc import ABC, abstractmethod
import zipfile
import os
import regex_ops

class ArchiveMixin:
    """A mixin to provide zip archiving functionality."""

    def archive_results(self, source_file: str, zip_name: str):
        """Archives a given file into a zip archive.

        Args:
            source_file (str): Path to the file to be archived.
            zip_name (str): The name of the output zip file.

        Raises:
            FileNotFoundError: If the source_file does not exist.
        """
        try:
            with zipfile.ZipFile(zip_name, 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(source_file, os.path.basename(source_file))
            print(f"[LOG]: File successfully archived in '{zip_name}'.")
        except FileNotFoundError:
            print(f"[ERROR]: Could not find file '{source_file}' to archive.")
        except Exception as e:
            print(f"[ERROR]: An unexpected error occurred during archiving: {e}")

class BaseAnalyzer(ABC):
    """Abstract base class for text analysis operations."""

    def __init__(self, text: str):
        """Initializes the analyzer with text.

        Args:
            text (str): The raw text to be analyzed.
        """
        self._text = text

    @property
    def text(self) -> str:
        """str: Getter for the analyzer's text."""
        return self._text

    @text.setter
    def text(self, value: str):
        """Sets the text for the analyzer.

        Args:
            value (str): The text string to set.

        Raises:
            ValueError: If the provided text is empty.
        """
        if not value:
            raise ValueError("Text content cannot be empty.")
        self._text = value

    @abstractmethod
    def run_full_analysis(self) -> dict:
        """Abstract method to perform text analysis."""
        pass

class AdvancedTextAnalyzer(BaseAnalyzer, ArchiveMixin):
    """Specific implementation of text analysis using regex operations."""

    def __init__(self, text: str):
        """Initializes the advanced analyzer.

        Args:
            text (str): The text to be processed.
        """
        super().__init__(text)
        self.results = {}

    def run_full_analysis(self) -> dict:
        """Executes the full suite of regex-based text analysis.

        Returns:
            dict: Formatted results including counts and filtered text.
        """
        current_text = self._text
        
        dec, ques, imp = regex_ops.count_sentences(current_text)
        avg_sent, avg_word = regex_ops.get_avg_lengths(current_text)
        v_word, v_pos = regex_ops.find_v_word(current_text)
        
        self.results = {
            "Sentence statistics": f"Dec: {dec}, Ques: {ques}, Imp: {imp}",
            "Average sentence length": round(avg_sent, 2),
            "Average word length": round(avg_word, 2),
            "Smiley count": regex_ops.get_smiley_count(current_text),
            "Mixed lowercase-digit words": regex_ops.find_lowercase_digit_words(current_text),
            "Total lowercase letters": regex_ops.count_lowercase_letters(current_text),
            "First 'v' word": f"'{v_word}' at index {v_pos}" if v_word else "None",
            "Filtered text (no 's' words)": regex_ops.remove_s_words(current_text)
        }
        return self.results

    def __str__(self) -> str:
        """Returns a string representation of the analyzer.

        Returns:
            str: A preview of the text being analyzed.
        """
        preview = self._text[:30] + "..." if len(self._text) > 30 else self._text
        return f"AdvancedTextAnalyzer handling text: [{preview}]"