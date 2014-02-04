$termOne = 1
$termTwo = 2
$sum = 2

while $termOne + $termTwo < 4000000 do
	$newTerm = $termOne + $termTwo
	if $newTerm % 2 == 0
		$sum += $newTerm
	end
	$termOne = $termTwo
	$termTwo = $newTerm
end

puts $sum
