// Here is the same solution only using Rust
use std::collections::HashMap;

impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        let mut occurances_map = HashMap::new();
        for elem in nums {
            if occurances_map.contains_key(&elem) {
                return true;
            }
            occurances_map.insert(elem, true);
        }
        return false;
    }
}
