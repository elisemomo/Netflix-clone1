def format_output(self, sgrep_out):
    if not sgrep_out:
        print("No results found.")
        return

    results = sgrep_out.json()
    if not results or 'results' not in results:
        print("No results found in the output.")
        return

    for find in results['results']:
        # Process each finding
        pass
