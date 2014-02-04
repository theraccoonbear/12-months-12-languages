$seed = 600851475141.0
$primes = []

while $seed > 1 do
	#work our way up from 2,
	#progressively knocking out
	#larger & larger primes
	for i in 2..$seed
		if $seed % i == 0.0
			$primes.push(i)
			$seed = $seed / i
			break
		end
	end
end

puts $primes.inspect
