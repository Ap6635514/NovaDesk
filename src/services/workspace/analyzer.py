class WorkspaceAnalyzer:

    def summarize(self, results):

        return (
            f"""
Workspace Scan Complete

Folders : {results['folders']}
Files   : {results['files']}

Large Files   : {len(results['large_files'])}
Temp Files    : {len(results['temp_files'])}
Empty Folders : {len(results['empty_folders'])}
"""
        )