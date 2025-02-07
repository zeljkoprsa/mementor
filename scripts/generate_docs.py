#!/usr/bin/env python3
import pystache
from pathlib import Path
from datetime import datetime

def generate_active_context():
    template_path = Path('templates/active_context.mustache')
    output_path = Path('docs/mementor_docs/activeContext.md')
    
    context = {
        'project_name': 'Mementor',
        'current_date': datetime.now().strftime('%Y-%m-%d'),
        'decisions': [
            'Fixed dependency installation issues',
            'Simplified template system implementation',
            'Added direct pystache integration'
        ],
        'next_steps': [
            {'description': 'Implement snapshot metadata', 'completed': False},
            {'description': 'Add decision tracing', 'completed': False},
            {'description': 'Enhance template system', 'completed': True}
        ]
    }
    
    if template_path.exists():
        template = template_path.read_text()
        renderer = pystache.Renderer()
        rendered = renderer.render(template, context)
        output_path.write_text(rendered)
        print(f"Successfully generated {output_path}")
    else:
        print(f"Template file not found: {template_path}")

if __name__ == '__main__':
    generate_active_context()
