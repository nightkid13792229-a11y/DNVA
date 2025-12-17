#!/usr/bin/env python3
"""
DNVA - DogNutritionVideoAuto
Minimal CLI for MVP phase
"""

import argparse
import os
import sys
from datetime import datetime
import random
import json

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
if PARENT_DIR not in sys.path:
    sys.path.insert(0, PARENT_DIR)

from dnva.core import ingest as ingest_core


def generate_run_id():
    """Generate unique run_id with timestamp + random suffix"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    random_suffix = ''.join(random.choices('0123456789abcdef', k=6))
    return f"{timestamp}_{random_suffix}"


def create_run_directories(run_id):
    """Create directory structure for a run"""
    base_path = os.path.join("storage", "runs", run_id)
    subdirs = [
        "ingest",
        "topicgen",
        "scriptgen",
        "assets",
        "draft",
        "publish_pack"
    ]
    
    for subdir in subdirs:
        dir_path = os.path.join(base_path, subdir)
        os.makedirs(dir_path, exist_ok=True)
    
    return base_path


def write_placeholder(path, content):
    """Write a placeholder file"""
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(content, f, indent=2, ensure_ascii=False)


def run_ingest(run_id):
    """Execute ingest step"""
    print(f"[INGEST] Starting ingest step for run_id: {run_id}")
    
    base_path = create_run_directories(run_id)
    result = ingest_core.run_ingest(run_id, base_path)
    
    print(f"[INGEST] Created directory: {os.path.join(base_path, 'ingest')}")
    print(f"[INGEST] Wrote items to: {result['items_path']}")
    print(f"[INGEST] Wrote sources to: {result['sources_path']}")
    print(f"[INGEST] Items count: {result['item_count']}")
    print(f"[INGEST] Run ID: {run_id}")
    return run_id


def run_topicgen(run_id):
    """Placeholder for topicgen step"""
    print(f"[TOPICGEN] Starting topicgen step for run_id: {run_id}")
    
    base_path = create_run_directories(run_id)
    topicgen_path = os.path.join(base_path, "topicgen")
    
    # Create placeholder file
    placeholder = {
        "run_id": run_id,
        "step": "TOPICGEN",
        "created_at": datetime.now().isoformat(),
        "status": "placeholder",
        "note": "This is a placeholder for PR-0. Real implementation in PR-2."
    }
    
    write_placeholder(os.path.join(topicgen_path, "placeholder.json"), placeholder)
    
    print(f"[TOPICGEN] Created directory: {topicgen_path}")
    print(f"[TOPICGEN] Wrote placeholder file")
    print(f"[TOPICGEN] Run ID: {run_id}")
    return run_id


def run_scriptgen(run_id):
    """Placeholder for scriptgen step"""
    print(f"[SCRIPTGEN] Starting scriptgen step for run_id: {run_id}")
    
    base_path = create_run_directories(run_id)
    scriptgen_path = os.path.join(base_path, "scriptgen")
    
    # Create placeholder file
    placeholder = {
        "run_id": run_id,
        "step": "SCRIPTGEN",
        "created_at": datetime.now().isoformat(),
        "status": "placeholder",
        "note": "This is a placeholder for PR-0. Real implementation in PR-4."
    }
    
    write_placeholder(os.path.join(scriptgen_path, "placeholder.json"), placeholder)
    
    print(f"[SCRIPTGEN] Created directory: {scriptgen_path}")
    print(f"[SCRIPTGEN] Wrote placeholder file")
    print(f"[SCRIPTGEN] Run ID: {run_id}")
    return run_id


def run_assets(run_id):
    """Placeholder for assets step"""
    print(f"[ASSETS] Starting assets step for run_id: {run_id}")
    
    base_path = create_run_directories(run_id)
    assets_path = os.path.join(base_path, "assets")
    
    # Create placeholder file
    placeholder = {
        "run_id": run_id,
        "step": "ASSETS",
        "created_at": datetime.now().isoformat(),
        "status": "placeholder",
        "note": "This is a placeholder for PR-0. Real implementation in PR-5."
    }
    
    write_placeholder(os.path.join(assets_path, "placeholder.json"), placeholder)
    
    print(f"[ASSETS] Created directory: {assets_path}")
    print(f"[ASSETS] Wrote placeholder file")
    print(f"[ASSETS] Run ID: {run_id}")
    return run_id


def run_draft(run_id):
    """Placeholder for draft step"""
    print(f"[DRAFT] Starting draft step for run_id: {run_id}")
    
    base_path = create_run_directories(run_id)
    draft_path = os.path.join(base_path, "draft")
    
    # Create placeholder file
    placeholder = {
        "run_id": run_id,
        "step": "DRAFT",
        "created_at": datetime.now().isoformat(),
        "status": "placeholder",
        "note": "This is a placeholder for PR-0. Real implementation in PR-6."
    }
    
    write_placeholder(os.path.join(draft_path, "placeholder.json"), placeholder)
    
    print(f"[DRAFT] Created directory: {draft_path}")
    print(f"[DRAFT] Wrote placeholder file")
    print(f"[DRAFT] Run ID: {run_id}")
    return run_id


def run_publishpack(run_id):
    """Placeholder for publishpack step"""
    print(f"[PUBLISHPACK] Starting publishpack step for run_id: {run_id}")
    
    base_path = create_run_directories(run_id)
    publishpack_path = os.path.join(base_path, "publish_pack")
    
    # Create placeholder file
    placeholder = {
        "run_id": run_id,
        "step": "PUBLISHPACK",
        "created_at": datetime.now().isoformat(),
        "status": "placeholder",
        "note": "This is a placeholder for PR-0. Real implementation in PR-7."
    }
    
    write_placeholder(os.path.join(publishpack_path, "placeholder.json"), placeholder)
    
    print(f"[PUBLISHPACK] Created directory: {publishpack_path}")
    print(f"[PUBLISHPACK] Wrote placeholder file")
    print(f"[PUBLISHPACK] Run ID: {run_id}")
    return run_id


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="DNVA - DogNutritionVideoAuto CLI (MVP)",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # run command
    run_parser = subparsers.add_parser('run', help='Run a specific step')
    run_parser.add_argument(
        '--step',
        required=True,
        choices=['ingest', 'topicgen', 'scriptgen', 'assets', 'draft', 'publishpack'],
        help='Step to execute'
    )
    
    args = parser.parse_args()
    
    if args.command == 'run':
        # Generate new run_id for this execution
        run_id = generate_run_id()
        
        # Execute the requested step
        step_handlers = {
            'ingest': run_ingest,
            'topicgen': run_topicgen,
            'scriptgen': run_scriptgen,
            'assets': run_assets,
            'draft': run_draft,
            'publishpack': run_publishpack
        }
        
        handler = step_handlers.get(args.step)
        if handler:
            handler(run_id)
        else:
            print(f"Error: Unknown step '{args.step}'", file=sys.stderr)
            sys.exit(1)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
