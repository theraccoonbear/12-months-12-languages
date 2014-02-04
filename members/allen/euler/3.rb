$seed = 600851475143.0
$largest_prime

while $seed > 1 do
	#work our way up from 2,
	#progressively knocking out
	#larger & larger primes
	for i in 2..$seed
		if $seed % i == 0.0
			$largest_prime = i
			$seed = $seed / i
			break
		end
	end
end

puts $largest_prime
