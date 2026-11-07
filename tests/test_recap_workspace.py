"""Recap workspace layout and shared-source hand-off regression tests."""
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class RecapWorkspaceLayoutTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.controller = (ROOT / "app" / "controller.py").read_text(encoding="utf-8")
        cls.splitter = (ROOT / "app" / "splitter_tab.py").read_text(encoding="utf-8")

    def test_related_tools_live_inside_the_single_recap_workspace(self):
        self.assertIn("self.workspace_tabs = ttk.Notebook(recap_tab", self.controller)
        self.assertIn('self.tools_tabs.add(recap_tab, text="Recap")', self.controller)
        for widget, label in (
            ("recap_workspace_tab", "Production"),
            ("studio_tab", "Downloader / Studio"),
            ("thumbnail_tab", "Thumbnail"),
            ("subtitle_tools_tab", "Subtitles / Subbing"),
            ("dubbing_tab", "Character Dubbing"),
            ("project_tools_tab", "Project / Audio"),
            ("recap_queue_tab", "Recap Queue"),
            ("splitter_tab", "Splitter"),
        ):
            self.assertIn(
                f'self.workspace_tabs.add(self.{widget}, text="{label}")',
                self.controller,
            )
        self.assertNotIn('self.tools_tabs.add(self.studio_tab', self.controller)
        self.assertNotIn('self.tools_tabs.add(self.thumbnail_tab', self.controller)
        self.assertNotIn('self.tools_tabs.add(self.splitter_tab', self.controller)

    def test_downloaded_video_returns_to_recap_production(self):
        self.assertIn("self.workspace_tabs.select(self.recap_workspace_tab)", self.controller)
        self.assertIn("self._sync_recap_source_to_tools()", self.controller)

    def test_recap_source_is_shared_with_relevant_tool_pages(self):
        for reference in (
            "follow_recap_source(self.thumbnail_tab.video)",
            "follow_recap_source(self.subtitle_tools_tab.video_path)",
            "follow_recap_source(self.dubbing_tab.source)",
            "self.splitter_tab.add_source_video(source)",
        ):
            self.assertIn(reference, self.controller)

    def test_splitter_has_a_safe_shared_source_entry_point(self):
        self.assertIn("def add_source_video(self, path: str | Path)", self.splitter)
        self.assertIn("candidate = Path(path).expanduser().resolve()", self.splitter)
        self.assertIn("self._add([candidate])", self.splitter)


if __name__ == "__main__":
    unittest.main()
