import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


class MapTest(unittest.TestCase):
    def test_export_and_invalid_update(self):
        script = Path(__file__).resolve().parents[1] / "scripts/map.py"
        with tempfile.TemporaryDirectory() as temp:
            state = Path(temp)
            (state / "records").mkdir()
            meta = {"project": "</script>ą", "period": "2027", "private": "private marker"}
            (state / "project.json").write_text(json.dumps(meta))
            output = state / "map.html"
            command = [sys.executable, script, state, output]
            subprocess.run(command, check=True, capture_output=True)
            original = output.read_text(encoding="utf-8")
            self.assertNotIn("private marker", original)
            self.assertNotIn(meta["project"], original)
            (state / "records/broken.json").write_text("{}")
            failed = subprocess.run(command, capture_output=True, text=True)
            self.assertNotEqual(failed.returncode, 0)
            self.assertIn("broken.json", failed.stderr)
            self.assertEqual(output.read_text(encoding="utf-8"), original)
