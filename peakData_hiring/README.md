# PeakData hiring task solution

## Building & running a code

You can do it either using Jupyter Notebook (JN) or a Python script (after a conversion of JN to Python). A prerequisite is having git installed.

### Jupyter Notebook

<ol>
    <li>Download & instal conda following <a href="https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html#installing-conda-on-a-system-that-has-other-python-installations-or-packages">instructions from conda docs page</a>.</li>
    <li>Install JN acc. to <a href="https://jupyter.org/install">its installation manual on JN page</a>.</li>
    <li>Download the project files with <code>git clone https://github.com/tomfidos/python.git</code>.</li>
    <li>Start JN with <code>jupyter-lab</code> and import a file with the code <code>main.ipynb</code>.</li>
    <li>As a desired result csv is also commited to the repo remove it for the needs of this test.</li>
    <li>Open the file and run the code with choosing in the menu <code>Run -> Run All</code>.</li>
</ol>

### Python

<ol>
    <li>Download & install Python following: <a href="https://www.python.org/downloads/">https://www.python.org/downloads/</a>.</li>
    <li>Download the project files with <code>git clone https://github.com/tomfidos/python.git</code>.</li>
    <li>Convert <code>main.ipynb</code> file to Python script with: <code>jupyter nbconvert --to script main.ipynb</code> or simply use an alraedy prepared & commited <code>main.py</code></li>
    <li>As a desired result csv is also commited to the repo remove for the needs of this test.</li>
    <li>Assuming that you're in the source code directory run the code with <code>python3 main.py</code>.</li>
</ol>

## Approach

<ol>
    <li>I don't make sure that publication titles are unique because our goal is a list of unique authors and we'll deduplicate it anyway.</li>
    <li>I don't consider middle names.</li>
    <li>I don't compare same surnames for their first names when one record has got a full name provided and another has got just the first name initial letter.</li>
    <li>I convert an author list to Pandas Series and take advantage of <em>apply</em> method in order to optimize performance.</li>
    <li>I assume that an author full name has got always following order: first name (can be just initials), middle name (optionally; can be just initials) and last name.</li>
    <li>In order to compare strings successfully I change all to lowercase.</li>
</ol>

## Potential failures & bottlenecks

<ol>
    <li>It's possible that an author full name has got different order that in <b>Approach.6</b>.</li>
    <li>Regarding the middle names: Taking them into account can result in having a different list.</li>
    <li>With the current approach an author that once is described with full first name (and of course a last name) and another time with initials instead of the first name will be handled as two different persons.</li>
    <li>The same author will be treated as two different persons if there's a small difference in spelling, ex Kowalczyk vs Kovalczyk.</li>
</ol>

## Possible future amendments

<ol>
    <li>Taking the middle names into account</li>
    <li>Handle case described in <b>Potential failures & bottlenecks.3</b>: Compare full first names with initials. If an initial matches with the first name first letter we can consider authors to be the same person</li>
    <li>In case of having cloud environment, ex AWS, on our disposal we can automate the unique author list (assuming that the source file changes from time to time). Namely we can migrate this script to Lambda and trigger it with Step Functions cron job. The lambda can drop result files to stakeholders on emails, Slack, etc.</li>
    <li>Also we can update a Redshift table with the unique authors and make it accessible to non-technical users by some BI tool.</li>
    <li>The source file could be uploaded (when its new version appears) to S3 bucket. Then we can create one lambda that would check for change and insert/update a source data Redshift table. Another lambda would transform this data and update to the final Redshift table mentioned in point 2.</li>
    <li>Such solutions would require Serverless Framewrok configuration to manage and deploy lambdas and resources created ex in Terraform.</li>
</ol>
