
def count_batteries_by_health(present_capacities):
  # creating dictionary for the classification 
  classify = {"healthy": 0,
               "exchange": 0,
               "failed": 0}

  #claculating the SoH for each 'present capacity'
  for i in present_capacities:
    SoH = 100 * i / 120
    if SoH >= 80 and SoH <=100:
      classify["healthy"] += 1
    elif SoH >= 62 and SoH < 80:
      classify["exchange"] += 1
    else:
      classify["failed"] += 1

  return classify



def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
