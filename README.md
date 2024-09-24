# ABSTRACT :- 
This research is the integration of a set of elements in a system of capturing, processing, and digital image analysis. It allows a better visual and numeric interpretation to determine the toughness, ductility percentage, and fragility of steel AISI/SAE 1020 and 30, getting better qualitative and quantitative observation of the results from the impact test (Charpy test). Patterns in the standard form, ASTM E23, were digitalized to evaluate the percentage of ductility/fragility of specimen testing. After, we calculated the area and the equivalent diameter of the material. using digital image processing and numerical comparison between the patterns specified in the standard form ASTM E23 and the testing in the impact test , and it allows to find the kind of pattern it is closest and determine which degree of ductility. Finally, the results were compared by three experts. The algorithm accuracy was 80%.

# PROBLEM STATEMENT AND MOTIVATION :- 
Determining ductility and brittleness of materials accurately is crucial for various engineering applications. While standard tensile tests provide valuable insights, they often lack the dynamic loading conditions present in real-world scenarios. This gap necessitates a reliable method to assess a material's behavior under impact loads.
The current project focuses on utilizing the Charpy impact test to effectively determine the ductility and brittleness of materials. Here's why this project holds significant importance:
Safety-Critical Applications: Understanding a material's ductility and brittleness is paramount in industries like construction, transportation, and pressure vessel manufacturing. These industries rely on materials that can withstand sudden impacts without catastrophic failure.
Ductile-to-Brittle Transition Temperature (DBTT): Charpy impact tests enable the identification of the DBTT, a critical temperature at which a material's behavior shifts from ductile to brittle. This information is vital for safe operation in environments with fluctuating temperatures.
Material Selection and Design Optimization: By quantifying ductility and brittleness, engineers can make informed decisions regarding material selection for specific applications. This leads to safer, more reliable, and potentially lighter designs.
Quality Control: Charpy impact tests serve as a quality control tool, ensuring materials meet the specified toughness requirements and minimizing the risk of unexpected failures.

# ABOUT THE PROJECT :- 
The brittle fractures leave behind larger, more noticeable patterns or marks on the broken surface compared to ductile fractures.
By taking pictures of the broken specimen surfaces after the impact test, and analyzing the sizes of the patterns or marks using image processing software, the researchers can figure out which regions were brittle fractures (larger patterns) versus ductile fractures (smaller, smoother patterns).
This allows them to calculate what percentage of the surface was brittle versus ductile without relying on a person's subjective judgment by just looking at the surface.
Using image analysis and comparing to reference pattern images avoids the inconsistencies that can happen when different people examine the same surface manually.
So in simple terms - larger crack/fracture patterns = brittle regions, while smoother torn areas = ductile regions. Image processing quantifies the sizes to estimate the brittle versus ductile percentages objectively.

# OBJECTIVES :-

1.Material Selection: You'll likely choose different materials (e.g., steel, aluminum) to analyze their ductile-to-brittle transition behavior.

2.Temperature Variation: Charpy tests are often conducted at various temperatures to pinpoint the ductile-to-brittle transition temperature (DBTT). This is the temperature at which a material's fracture behavior significantly changes.

3.Data Analysis: The impact energy values obtained from the tests will be plotted against temperature. This helps visualize the transition and identify the DBTT.

4.Fracture Surface Examination: Analyzing the fracture surfaces of the tested specimens can provide additional insights. Ductile fractures typically exhibit a rough, shear-like appearance, while brittle fractures are often smooth and flat.

## Additional Considerations :- 

1.Standards: Following established testing standards like ASTM E23 is crucial to ensure accurate and reproducible results.
2.Impact Testing Machine: The Charpy test requires specialized equipment to deliver the standardized impact load.
3.Safety Precautions: Proper safety protocols must be followed during sample preparation, testing, and handling fractured specimens.

# CONCLUSION :- 

The application of graphite in the ASI 304 specimens turned out to be an alternative determinant to carry out the image processing, allowing the software to differentiate the areas formed in the test and thus subsequently go on to make a numerical comparison with the areas formed and the Pattern image areas using Euclidean distance. Evaluation by expert in materials was the determining factor for determining the degree of reliability of the algorithm since it allowed to know with certainty which descriptor of form (Equivalent area or diameter) was ideal for carrying out this type of image processing. A very low error rate (20%) has been presented when area is used as a shape descriptor. However, it is valid clarify that the percentage of error is supported by the application of ranges discrete that the ASTM E23 standard has. Likewise, it was evidenced that the equivalent diameter is not the most adequate descriptor for this type of application, since the results were not in agreement with the results of the experts. External factors at the time of image capture is a critical factor since any anomaly that occurs at the time of capturing the image will affect the digital processing of images for this it is necessary to eliminate all the noises or factors outsiders involved in the scene An open problem is still precision, consistency and efficiency of the algorithm. Future work will be focused on the development of a sophisticated method of deriving an optimized high-precision matching result under the influence of noise and illumination sources
