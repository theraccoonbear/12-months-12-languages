#cannot get this one to work...
$candidate = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def factorial(n)
	(1..n).reduce(:*)
end

def array_fits_into(int, candidate)
	$isDivisible = true
	($candidate.length - 1).downto(0) do |i|
		if int % candidate[i] != 0
			$isDivisible = false
		end
	end
	$isDivisible
end

for i in 1..factorial(20)
	puts i.to_s + "	" + array_fits_into(i, $candidate).to_s
	if array_fits_into(i, $candidate)
		puts i
		break	
	end
end