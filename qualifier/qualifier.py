from typing import Any, List, Optional


def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """
    ...

    # Get max lengths of columns
    rowLengths = [[len(str(cell)) for cell in row] for row in rows]
    columns = len(rowLengths[0])
    colLengths = []
    for i in range(0,columns):
        colLengths.append([])
        for row in rowLengths:
            colLengths[i].append(row[i])
    maxColLengths = [max(length) for length in colLengths]

    table = ""

    # Top of table
    tableHead = "-"
    for maxColLength in maxColLengths:
        tableHead += "-"*(maxColLength+2)

    table += tableHead + "-\n"

    # Main area of table
    for row in rows:
        tableRow = ""
        for index, cell in enumerate(row):
            tableRow += "| "
            tableRow += str(cell)
            tableRow += " "*(maxColLengths[index]-len(str(cell))+1)
        tableRow += "|\n"
        table += tableRow
    print(table)

make_table([['Apple', 5], ['Banana', 3], ['Cherry', 7], ['Kiwi', 4], ['Strawberry', 6]])