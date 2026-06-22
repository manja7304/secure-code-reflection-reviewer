from src.agents.runner import run_agent

def test_reflection():
    out = run_agent('review', {'snippet_id': 'SNIP-003'})
    assert 'Verdict' in out['answer']
