def isPalindrome(array)
	if array.length == 0
		return false
	elsif array.length == 1
		#one character, must be a palindrome
		return true
	else
		#check if the outermost pair
		# of characters are the same
		if array[0] == array[array.length - 1]
			#they are the same, if the array is
			#of length 2 we're done
			if array.length == 2
				return true
			else
				#potential candidate found &
				#we still have work to do

				#slice up array, drop 1st and last entries
				$newArr = array.take(array.length - 1).drop(1)
				#recursively call isPalindrome
				isPalindrome($newArr)
			end
		else
			return false
		end
	end
end

$largestPalindrome = 0

999.downto(1) do |i|
	999.downto(1) do |j|
		$numberToTest = i * j
		$intAsArray = $numberToTest.to_s.split('')
		if isPalindrome($intAsArray)
			if $numberToTest > $largestPalindrome
				$largestPalindrome = $numberToTest
			end
		end
	end
end

puts $largestPalindrome
