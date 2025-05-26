HSN Code Validation Agent - Submission Package
=============================================

Contents:
---------
1. HSN_Code_Validation_Assignment_CLEAN_NoRepeatHeader.pdf
   - Detailed explanation of the agent design using the ADK framework.
   - Includes data handling strategy, validation logic, agent response format, and enhancement ideas.

2. read_hsn.py
   - Python script simulating the validation logic described in the design.
   - Reads an Excel file and validates HSN codes provided by the user.

3. HSN_Master_Data.xlsx
   - Excel dataset containing valid HSN codes and their descriptions.

4. README.txt
   - Instructions for running the Python script.

Run Instructions:
-----------------
1. Ensure Python 3 is installed on your system.
2. Install dependencies by running this in your terminal:
   pip install pandas openpyxl

3. Place `read_hsn.py` and `HSN_Master_Data.xlsx` in the same folder.

4. Run the script:
   python read_hsn.py

5. When prompted, enter one or more HSN codes (comma-separated) to validate.

Example Input:
--------------
0101, 9999, abc, 01

Expected Output:
----------------
✅ 0101: VALID – LIVE HORSES, ASSES, MULES AND HINNIES.
❌ 9999: INVALID – Code not found in dataset.
❌ abc: INVALID – Not numeric.
✅ 01: VALID – LIVE ANIMALS

Contact:
--------
For any clarifications or demonstration, please refer to the submitted design document.
