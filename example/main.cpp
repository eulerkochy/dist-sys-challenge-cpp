#include <boost/json.hpp>
#include <iostream>

namespace json = boost::json;

int main() {
  // Create a JSON object
  json::object obj;
  obj["message"] = "Hello world!";
  obj["number"] = 42;
  obj["array"] = json::array{1, 2, 3};

  // Serialize to string
  std::string json_str = json::serialize(obj);
  std::cout << "JSON: " << json_str << std::endl;

  // Parse JSON from string
  json::value parsed = json::parse(json_str);
  std::cout << "Parsed message: " << parsed.at("message").as_string()
            << std::endl;

  return 0;
}
