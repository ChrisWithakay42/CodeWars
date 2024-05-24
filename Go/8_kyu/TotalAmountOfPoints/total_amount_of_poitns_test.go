package totalamountofpointstest

func TestCalculatePoints(t *testing.T) {
  tests := []struct{
    testName string
    matches []string
    expected int
  }{
    {testName: "all wins", matches: []string{"3:1", "3:2", "2:1"}, expected: 9},
{testName: "all losses", matches: []string{"2:3", "1:3}}
  }
}
