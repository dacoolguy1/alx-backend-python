def canUnlockAll(boxes):
  """
  Determines if all the boxes can be opened.

  Args:
    boxes: A list of lists
    A key with the same number as a box opens that box
    You can assume all keys will be positive integers
    There can be keys that do not have boxes
    The first box boxes[0] is unlocked
  Returns:
    True if all boxes can be opened, else False
  """

  # Initialize a list to track which boxes are unlocked.
  unlocked = [False] * len(boxes)

  # Recursively check if all boxes can be opened, starting from the second box.
  for i in range(1, len(boxes)):
    if not unlocked[i]:
      # If the box is not unlocked, check if it can be unlocked with any of the keys in the other boxes.
      for key in boxes[i]:
        if key < len(boxes) and unlocked[key]:
          unlocked[i] = True
          break

  # Return True if all boxes are unlocked, else False.
  return all(unlocked)

