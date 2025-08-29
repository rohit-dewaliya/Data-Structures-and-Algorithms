class Solution:
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        m = len(landStartTime)
        n = len(waterStartTime)

        # Step 1: Get the minimum land ride finish time
        min_land_end = float("inf")
        for i in range(m):
            min_land_end = min(min_land_end, landStartTime[i] + landDuration[i])

        # Step 2: Get the minimum water ride finish time
        min_water_end = float("inf")
        for j in range(n):
            min_water_end = min(min_water_end, waterStartTime[j] + waterDuration[j])

        # Step 3: Try land → water (start water after land finishes)
        min_finish_land_water = float("inf")
        for j in range(n):
            start_water = max(min_land_end, waterStartTime[j])
            end_water = start_water + waterDuration[j]
            min_finish_land_water = min(min_finish_land_water, end_water)

        # Step 4: Try water → land (start land after water finishes)
        min_finish_water_land = float("inf")
        for i in range(m):
            start_land = max(min_water_end, landStartTime[i])
            end_land = start_land + landDuration[i]
            min_finish_water_land = min(min_finish_water_land, end_land)

        # Step 5: Return the earliest finish of both combinations
        return min(min_finish_land_water, min_finish_water_land)
            
        
        '''
        min_finish_time = float('inf')

        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                start_land = landStartTime[i]
                end_land = start_land + landDuration[i]

                start_water = max(end_land, waterStartTime[j])
                end_water = start_water + waterDuration[j]
                min_finish_time = min(min_finish_time, end_water)

                start_water = waterStartTime[j]
                end_water = start_water + waterDuration[j]

                start_land = max(end_water, landStartTime[i])
                end_land = start_land + landDuration[i]
                min_finish_time = min(min_finish_time, end_land)

        return min_finish_time
        '''

landStartTime = [2,8]
landDuration = [4,1]
waterStartTime = [6]
waterDuration = [3]

print(Solution().earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration))
