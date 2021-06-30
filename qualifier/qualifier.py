from typing import Any, List, Optional

def stringify(cell):
    return str(cell)

def formatTableDivider(left, middle, right, maxColLengths):
    tableHead = left
    for index, maxColLength in enumerate(maxColLengths):
        tableHead += "─"*(maxColLength+2)
        if index < len(maxColLengths)-1:
            tableHead += middle

    return tableHead + right +"\n"

def tableContent(row, maxColLengths, centered):
    tableRow = ""
    for index, cell in enumerate(row):
        tableRow += "│ "
        if centered:
            padding = ((maxColLengths[index]-len(stringify(cell)))/2)
            leftPadding = int(padding)
            rightPadding = leftPadding + 1 if padding == float(leftPadding) else leftPadding + 2

            tableRow += " "*leftPadding
            tableRow += stringify(cell)
            tableRow += " "*rightPadding
        else:
            tableRow += stringify(cell)
            tableRow += " "*(maxColLengths[index]-len(stringify(cell))+1)
    return tableRow + "│\n"
    

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
    rowLengths = [[len(stringify(cell)) for cell in row] for row in rows]
    columns = len(rowLengths[0])
    colLengths = []
    for i in range(0,columns):
        colLengths.append([])
        for row in rowLengths:
            colLengths[i].append(row[i])
    maxColLengths = [max(length) for length in colLengths]

    if labels is not None:
        for index, maxColLength in enumerate(maxColLengths):
            label = stringify(labels[index])
            if len(label) > maxColLength:
                maxColLengths[index] = len(label)

    # Setup table
    table = ""

    # Top of table
    table += formatTableDivider("┌","┬","┐",maxColLengths)
    
    # Add labels
    if labels is not None:
        table += tableContent(labels, maxColLengths, centered)

        table += formatTableDivider("├","┼","┤",maxColLengths)

    # Main area of table
    for row in rows:
        table += tableContent(row, maxColLengths, centered)

    # Bottom of table
    table += formatTableDivider("└","┴","┘",maxColLengths)

    print(table)
    return table